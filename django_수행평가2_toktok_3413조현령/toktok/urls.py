from django.urls import path

from toktok import views

app_name = 'toktok'

urlpatterns = [
    path('', views.index, name='index'),  # toktok:Index
    path('repository/', views.RepositoryListView.as_view(), name='repository_list'),    #toktok:repository_list
    path('repository/<int:pk>/', views.RepositoryDetailView.as_view(), name='repository_detail'),    #toktok:repository_detail
    path('repository/<int:repository_pk>/introduction/<int:pk>/', views.IntroductionDetailView.as_view(), name='introduction_detail'),    #toktok:introduction_detail
    path('repository/add/', views.RepositoryCreateView.as_view(), name='repository_add'),    #toktok:repository_add
    path('repository/<int:pk>/modify/', views.RepositoryUpdateView.as_view(), name='repository_modify'),    #toktok:repository_modify
    path('repository/<int:pk>/delete/', views.RepositoryDeleteView.as_view(), name='repository_delete'),    #toktok:repository_delete
    path('repository/<int:repository_pk>/introduction/add/', views.add_introduction, name='introduction_add'),
    path('repository/<int:repository_pk>/introduction/<int:pk>/modify/', views.IntroductionUpdateView.as_view(), name='introduction_modify'),
    path('repository/<int:repository_pk>/introduction/<int:pk>/delete/', views.IntroductionDeleteView.as_view(), name='introduction_delete'),
    path('repository/<int:repository_pk>/introduction/<int:introduction_pk>/comment/add/', views.CommentCreateView.as_view(), name='comment_add'),
    path('repository/<int:repository_pk>/introduction/<int:introduction_pk>/comment/<int:pk>/modify/', views.CommentUpdateView.as_view(), name='comment_modify'),
    path('repository/<int:repository_pk>/introduction/<int:introduction_pk>/comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]