from django import forms

from begin_vegan.models import Post, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'title', 'content', 'category', 'photo']


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['user', 'post', 'comment']

