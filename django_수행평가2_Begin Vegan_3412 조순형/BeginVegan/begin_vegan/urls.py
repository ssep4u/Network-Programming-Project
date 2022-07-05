from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from begin_vegan import views

app_name = 'begin_vegan'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('post/', views.post, name='post'),
    path('category/post/list', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/modify/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:post_pk>/comment/create/', views.CommentsCreateView.as_view(), name='comment_create'),
    path('post/<int:post_pk>/comment/<int:pk>/modify/', views.CommentsUpdateView.as_view(), name='comment_update'),
    path('post/<int:post_pk>/comment/<int:pk>/delete/', views.CommentsDeleteView.as_view(), name='comment_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)