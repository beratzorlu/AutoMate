from django.db import models
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    This class defines the db model for the posts.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    excerpt = models.TextField(max_length=100, blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
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

    def get_absolute_url(self):
        return reverse('post_detail', args={self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Defines the db models for comment posts.
    """
    name = models.CharField(max_length=32)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment_author', )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
