from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from accounts.models import Profile
from begin_vegan.models import Post, Comments


def index(request):
    return render(request, 'begin_vegan/index.html')


def header(request):
    return render(request, 'begin_vegan/header.html')


def category(request):
    return render(request, 'begin_vegan/category.html')


def post(request):
    if request.GET.get('category') == '비건':
        post_list = Post.objects.filter(category='비건')
        context = {'post_list': post_list}
        return render(request, 'begin_vegan/post_list.html', context)
    elif request.GET.get('category') == '락토-오보':
        post_list = Post.objects.filter(category='락토-오보')
        context = {'post_list': post_list}
        return render(request, 'begin_vegan/post_list.html', context)
    elif request.GET.get('category') == '페스코':
        post_list = Post.objects.filter(category='페스코')
        context = {'post_list': post_list}
        return render(request, 'begin_vegan/post_list.html', context)
    elif request.GET.get('category') == '폴로':
        post_list = Post.objects.filter(category='폴로')
        context = {'post_list': post_list}
        return render(request, 'begin_vegan/post_list.html', context)
    elif request.GET.get('category') == '플렉시테리언':
        post_list = Post.objects.filter(category='플렉시테리언')
        context = {'post_list': post_list}
        return render(request, 'begin_vegan/post_list.html', context)


class PostListView(generic.ListView):
    model = Post


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ['user', 'title', 'content', 'category', 'photo']
    template_name_suffix = '_create'
    success_url = reverse_lazy('begin_vegan:post_list')

    def get_initial(self):
        user = self.request.user
        user = Profile.objects.get(user=user)
        return {'user': user}


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = ['user', 'title', 'content', 'category', 'photo']
    template_name_suffix = '_update'
    success_url = reverse_lazy('begin_vegan:post_list')


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy('begin_vegan:post_list')


class CommentsCreateView(generic.CreateView):
    model = Comments
    fields = ['user', 'post', 'comment']
    template_name_suffix = '_create'

    def get_initial(self):
        user = self.request.user
        user = Profile.objects.get(user=user)

        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])

        return {'user': user, 'post': post}

    def get_success_url(self):
        kwargs = {
            'pk': self.kwargs['post_pk'],
        }
        return reverse_lazy('begin_vegan:post_detail', kwargs=kwargs)


class CommentsUpdateView(generic.UpdateView):
    model = Comments
    fields = ['user', 'post', 'comment']
    template_name_suffix = '_update'

    def get_success_url(self):
        kwargs = {
            'pk': self.kwargs['post_pk'],
        }
        return reverse_lazy('begin_vegan:post_detail', kwargs=kwargs)


class CommentsDeleteView(generic.DeleteView):
    model = Comments

    def get_success_url(self):
        kwargs = {
            'pk': self.kwargs['post_pk'],
        }
        return reverse_lazy('begin_vegan:post_detail', kwargs=kwargs)

