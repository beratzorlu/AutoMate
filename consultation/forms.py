from .models import Consultation
from crispy_forms.helper import FormHelper
from django import forms


class ApplicationForm(forms.ModelForm):
    """
    Defines the model for the application form
    """
    class Meta:
        model = Consultation
        fields = ('first_name', 'last_name', 'author', 'birthdate', 'email', 'fav_maker', 'budget', 'purpose', 'status')