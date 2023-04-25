from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import generic, View


class PostList(generic.ListView):
    """
    Class-based view of the Post model
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class DetailView(View):
    """
    Class-based view of the detailed post views
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by['-created_on']
        is_liked = False
        if post.likes.filter(self.request.user.id).exists():
            is_liked = True
        model = Post
        template_name = 'post_detail.html'

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "is_liked": is_liked,
            },
        )
