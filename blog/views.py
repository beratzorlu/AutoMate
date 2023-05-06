from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post, Comment
from django.views import generic, View
from .forms import UserCommentForm, UserPostEditForm, UserAddPostForm
from django.urls import reverse_lazy


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
            messages.success(request, "Success! Your comment has been submitted and waiting admin approval.")
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


class UserPostDelete(generic.DeleteView):
    """
    Class-based view for deleting blog posts
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog_list')


class UserPostEdit(generic.UpdateView):
    """
    Class-based view for editing and updating blog posts.
    """
    model = Post
    template_name = 'edit_post.html'
    form_class = UserPostEditForm

    def redirect_postdetail(self):
        return redirect(reverse("post_detail", args=[comment.post.slug]))


class UserPostAdd(generic.CreateView):
    """
    Class-based view for creating new blog posts.
    """
    model = Post
    template_name = 'add_post.html'
    form_class = UserAddPostForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        return super(UserPostAdd, self).form_valid(form)


def delete_comment(request, comment_id):
    """
    Function-based view for deleting comments.
    """
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.name == request.user.username:
        comment.delete()
        messages.success(request, "Your comment has been deleted.")
        return redirect(reverse("post_detail", args=[comment.post.slug]))
    else:
        messages.error(request, "You are not authorized to delete this comment.")
        return redirect(request.META.get('HTTP_REFERER', reverse('home')))


def edit_comment(request, comment_id):
    """
    Function-based view for editing comments.
    """
    template = "edit_comment.html"
    comment = get_object_or_404(Comment, id=comment_id)
    user_comment_form = UserCommentForm(request.POST or None, instance=comment)

    if request.method == "POST":
        if user_comment_form.is_valid():
            user_comment_form.save()
            messages.success(request, "Successfully saved your changes.")
            return redirect(reverse("post_detail", args=[comment.post.slug]))
        messages.error(request, "Sorry, something went wrong. Please try again.")
    
    context = {
        "comment": comment,
        "user_comment_form": user_comment_form,
    }

    return render(request, template, context)
    
