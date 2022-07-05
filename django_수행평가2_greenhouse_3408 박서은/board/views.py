from django.db.models import Max
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from board.forms import IntroductionForm
from board.models import Repository, Introduction, Comment


class RepositoryListView(generic.ListView):
    model = Repository


class RepositoryDetailView(generic.DetailView):
    model = Repository


class RepositoryCreateView(generic.CreateView):
    model = Repository
    fields = ['name', 'description', 'deadline']  # '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('board:repository_list')


class RepositoryUpdateView(generic.UpdateView):
    model = Repository
    fields = ['name', 'description', 'deadline']  # '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('board:repository_list')


class RepositoryDeleteView(generic.DeleteView):
    model = Repository
    success_url = reverse_lazy('board:repository_list')


class IntroductionDetailView(generic.DetailView):
    model = Introduction


class IntroductionCreateView(generic.CreateView):
    model = Introduction
    fields =  ['title', 'repository', 'number', 'contents', 'writer']   # '__all__'
    template_name_suffix = '_create'

    def get_initial(self):
        repository = get_object_or_404(Repository, pk=self.kwargs['repository_pk'])
        introduction = repository.introduction_set.aggregate(
            Max('number'))  # 해당 repository의 introduction 중 number 최대값 구하자
        number = introduction['number__max']
        if number == None:  # introduction이 아예 없으면 number 기본값: 1
            number = 1
        else:  # introduction이 있으면 number 최대값에서 +1
            number += 1
        return {'repository': repository, 'number': number}

    def get_success_url(self):
        return reverse_lazy('board:repository_detail', kwargs={'pk': self.kwargs['repository_pk']})


def add_introduction(request, repository_pk):  # return render(request, '템플릿 이름', 그템플릿에 넘겨주는 context)
    if request.method == 'POST':  # POST라면
        form = IntroductionForm(request.POST)  # introduction 만드는 form에서 입력한 정보 가져오자
        if form.is_valid():  # 그 정보가 확인되면
            form.save()  # DB에 저장
            return redirect('board:repository_detail', pk=repository_pk)  # repository_detail로 redirect
    else:  # POST가 아니면(요청한 것: introduction 만들기위한 form 보여주기)
        repository = get_object_or_404(Repository, pk=repository_pk)  # repository를 DB에서 꺼내자
        introduction = repository.introduction_set.order_by('-number').first()
        if introduction == None:
            number = 1  # introduction이 없으면 number = 1
            contents = ''  # introduction이 없으면 ''
            writer = 1
        else:
            number = introduction.number + 1  # repository에 있는 introduction 중 가장 큰 버전 + 1
            writer = introduction.writer
        initial = {'repository': repository, 'number': number}
        form = IntroductionForm(initial=initial)  # form 가져오자
        context = {'form': form, 'repository': repository}  # context = form, repository

    return render(request, 'board/introduction_create.html', context)


class IntroductionUpdateView(generic.UpdateView):
    model = Introduction
    template_name_suffix = '_update'
    fields = ['title', 'repository', 'number', 'contents', 'writer']  # '__all__'
    labels = {
        'title': '  글 제목',
        'repository': '  주제   ',
        'number': '  글 번호',
        'contents': '  글 내용',
        'writer': '  작성자',
    }

    def get_success_url(self):
        return reverse_lazy('board:repository_detail', kwargs={'pk': self.kwargs['repository_pk']})


class IntroductionDeleteView(generic.DeleteView):
    model = Introduction

    def get_success_url(self):
        return reverse_lazy('board:repository_detail', kwargs={'pk': self.kwargs['repository_pk']})


class CommentCreateView(
    generic.CreateView):  # repository/<int:repository_pk>/introduction/<int:introduction_pk>/comment/add/
    model = Comment
    fields = ['text', 'comment']  # ['introduction', 'comment']
    labels = {
        'text': '  글 제목',
        'comment': '  댓글   ',
    }
    template_name_suffix = '_create'  # comment_create.html

    def get_initial(self):
        text = get_object_or_404(Introduction, pk=self.kwargs['introduction_pk'])
        return {'text': text}

    def get_success_url(self):  # board:introduction_detail repository_pk pk
        kwargs = {
            'repository_pk': self.kwargs['repository_pk'],
            'pk': self.kwargs['introduction_pk'],
        }
        return reverse_lazy('board:introduction_detail',
                            kwargs=kwargs)  # repository/<int:repository_pk>/introduction/<int:pk>/


class CommentUpdateView(generic.UpdateView):
    model = Comment
    fields = ['text', 'comment']  # ['introduction', 'comment']
    labels = {
        'text': '  글 제목',
        'comment': '  댓글   ',
    }
    template_name_suffix = '_update'  # comment_update.html

    def get_success_url(self):  # board:introduction_detail repository_pk pk
        kwargs = {
            'repository_pk': self.kwargs['repository_pk'],
            'pk': self.kwargs['introduction_pk'],
        }
        return reverse_lazy('board:introduction_detail',
                            kwargs=kwargs)  # repository/<int:repository_pk>/introduction/<int:pk>/


class CommentDeleteView(generic.DeleteView):
    model = Comment

    def get_success_url(self):  # board:introduction_detail repository_pk pk
        kwargs = {
            'repository_pk': self.kwargs['repository_pk'],
            'pk': self.kwargs['introduction_pk'],
        }
        return reverse_lazy('board:introduction_detail',
                            kwargs=kwargs)  # repository/<int:repository_pk>/introduction/<int:pk>/
