from django.urls import path
from .views import PostListView, RatingCreateView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('ratings/', RatingCreateView.as_view(), name='rating'),
]
