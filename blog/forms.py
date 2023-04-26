from .models import Comment
from django import forms


class UserCommentForm(forms.ModelForm):
    """
    Defines the model for the comment form
    """
    class Meta:
        model = Comment
        fields = ('body', )
