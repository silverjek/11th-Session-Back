from .views import *
from django.urls import path

app_name = 'api'

urlpatterns=[
    path('posts/', PostListView.as_view()), #클래스형 함수 갖고 올 때는 .as_view() 붙여야 함!
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('comments/', CommentView.as_view()),
    path('comments/<int:pk>/', CommentDetailView.as_view()),
]