from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    auther = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    context = models.TextField(blank='')


class Rate(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=0, choices=[(i, str(i)) for i in range(6)])

