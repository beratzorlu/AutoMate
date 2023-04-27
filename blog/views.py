from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import Post
from django.views import generic, View
from .forms import UserCommentForm


class PostList(generic.ListView):
    """
    Class-based list view of the Post model
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class DetailView(View):
    """
    Class-based view of the detailed post detail page
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        is_liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            is_liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "is_liked": is_liked,
                "user_comment_form": UserCommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        is_liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            is_liked = True

        user_comment_form = UserCommentForm(data=request.POST)

        if user_comment_form.is_valid():
            user_comment_form.instance.email = request.user.email
            user_comment_form.instance.name = request.user.username
            comment = user_comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            user_comment_form = UserCommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "is_liked": is_liked,
                "user_comment_form": UserCommentForm()
            },
        )


class UserPostLike(View):
    """
    Class-based view for user likes on blog posts
    """

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
