from .models import Comment
from crispy_forms.helper import FormHelper
from django import forms


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

