from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView

from .models import Post, Rate
from .serializers import PostSerializer, RatingSerializer


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class RatingCreateView(CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.request.data.get('post')
        rating = self.request.data.get('rating')
        existing_rating = Rate.objects.filter(user=user, post_id=post_id).first()
        if existing_rating:
            existing_rating.rating = rating
            existing_rating.save()
        else:
            serializer.save(user=user)
