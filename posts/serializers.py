from django.db.models import Count, Avg
from rest_framework import serializers
from .models import Post, Rate


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    rated_users_count = serializers.ReadOnlyField()
    avg_rating = serializers.ReadOnlyField()
    user_rating = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'rated_users_count', 'avg_rating', 'user_rating')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        ratings_data = Rate.objects.filter(post=instance).aggregate(
            rated_users_count=Count('user'),
            avg_rating=Avg('rating')
        )

        data['rated_users_count'] = ratings_data['rated_users_count']
        data['avg_rating'] = ratings_data['avg_rating']

        user = self.context['request'].user
        if user.is_authenticated:
            data['user_rating'] = Rate.objects.filter(user=user, post=instance).values_list('rating', flat=True).first()
        else:
            data['user_rating'] = None
        return data
