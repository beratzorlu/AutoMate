from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    This class defines the db model for the posts.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_on']

    def likes_numbers(self):
        return self.likes.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Defines the db models for comment posts.
    """
    name = models.CharField(max_length=32)
    email = models.EmailField()
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
