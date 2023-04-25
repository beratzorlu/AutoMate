from django.shortcuts import render
from .models import Post
from django.views import generic


class PostList(generic.ListView):
    """
    Class-based view of the Post model
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class DetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
