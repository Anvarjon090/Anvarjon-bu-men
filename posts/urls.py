from django.urls import path

from posts.views import PostListAPIView, PostDetailAPIView, PostCreateAPIView


urlpatterns = [
    path('all/', PostListAPIView.as_view()),
    path('<int:pk>/', PostDetailAPIView.as_view()),
    path('create/', PostCreateAPIView.as_view()),
]