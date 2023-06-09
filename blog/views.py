from .models import Post, Comment
from django.views import generic, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from consultation.models import Consultation
from .forms import UserCommentForm, UserPostEditForm, UserAddPostForm


class PostList(generic.ListView):
    """
    Class-based list view of the PostList model
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class BlogList(generic.ListView):
    """
    Class-based list view of the BlogList model.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog_list.html'
    paginate_by = 8


class DetailView(LoginRequiredMixin, View):
    """
    Class-based view of the post detail page
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
            user_comment_form.instance.author = self.request.user
            user_comment_form.instance.name = request.user.username
            comment = user_comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, "Success! Your comment has been submitted and waiting admin approval.")  # noqa
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


class UserPostLike(LoginRequiredMixin, View):
    """
    Class-based view for user likes on blog posts
    """

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(request, "Like removed.")
        else:
            post.likes.add(request.user)
            messages.success(request, "Like added.")

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class UserPostDelete(LoginRequiredMixin, generic.DeleteView):
    """
    Class-based view for deleting blog posts
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_superuser  # noqa

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(status=1)

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_superuser:
            messages.success(self.request, 'Your blog has been successfully removed.')  # noqa
            return super(UserPostDelete, self).delete(request, *args, **kwargs)
        else:
            messages.warning(self.request, 'You are not authorized to delete posts of other users.')  # noqa
            return HttpResponseForbidden()


class UserPostEdit(LoginRequiredMixin, generic.UpdateView):
    """
    Class-based view for editing and updating blog posts.
    """
    model = Post
    template_name = 'edit_post.html'
    form_class = UserPostEditForm
    success_url = reverse_lazy('blog_list')

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_superuser:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(status=1)

    def form_valid(self, form):
        blogObject = self.get_object()
        post = form.save(commit=False)
        if self.request.user == post.author or self.request.user.is_superuser:
            post.save()
            messages.success(self.request, 'Success! Your changes have been saved.')  # noqa
            return redirect(reverse("blog_list"))
        else:
            messages.warning(self.request, 'You are not authorized to edit the posts of other users.')  # noqa
            return redirect(reverse("home"))


class UserPostAdd(LoginRequiredMixin, generic.CreateView):
    """
    Class-based view for creating new blog posts.
    """
    model = Post
    template_name = 'add_post.html'
    form_class = UserAddPostForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        if user.is_authenticated or user.is_superuser:
            messages.success(self.request, "Your blog has been published!")
            return super(UserPostAdd, self).form_valid(form)
        else:
            messages.warning(self.request, "Only authorized users can publish content!")  # noqa
            return HttpResponseRedirect(reverse('blog_list'))


@login_required
def delete_comment(request, comment_id):
    """
    Function-based view for deleting comments.
    """
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)

    if comment.name == request.user.username:
        comment.delete()
        messages.success(request, "Your comment has been deleted.")
        return redirect(reverse("post_detail", args=[comment.post.slug]))
    else:
        messages.error(request, "You are not authorized to delete this comment.")  # noqa
        return redirect(request.META.get('HTTP_REFERER', reverse('home')))


@login_required
def edit_comment(request, comment_id):
    """
    Function-based view for editing comments.
    """
    template = "edit_comment.html"
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    user_comment_form = UserCommentForm(request.POST or None, instance=comment)

    if request.method == "POST":
        if user_comment_form.is_valid():
            user_comment_form.save()
            messages.success(request, "Successfully saved your changes.")
            return redirect(reverse("post_detail", args=[comment.post.slug]))
        messages.error(request, "Sorry, something went wrong. Please try again.")  # noqa

    context = {
        "comment": comment,
        "user_comment_form": user_comment_form,
    }

    return render(request, template, context)
