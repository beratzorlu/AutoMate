from .models import Comment, Post
from crispy_forms.helper import FormHelper
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class UserCommentForm(forms.ModelForm):
    """
    Defines the model for the comment form
    """
    def __init__(self, *args, **kwargs):
        super(UserCommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = False

    class Meta:
        model = Comment
        fields = ('body', )


class UserPostEditForm(forms.ModelForm):
    """
    Defines the model for the blog edit form
    """
    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'mb-4 form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'mb-4 form-control'}),
            'content': forms.Textarea(attrs={'class': 'mb-4 form-control'}),
        }


class UserAddPostForm(forms.ModelForm):
    """
    Defines the model for the blog edit form
    """
    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'featured_image', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'mb-4 form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'mb-4 form-control'}),
            'content': forms.Textarea(attrs={'class': 'mb-4 form-control'}),
        }
