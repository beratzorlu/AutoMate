from .models import Consultation
from crispy_forms.helper import FormHelper
from django import forms


class ApplicationForm(forms.ModelForm):
    """
    Defines the model for the application form
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].disabled = True
        if self.fields['status'].disabled:
            self.fields['status'].default = 1

    class Meta:
        model = Consultation
        fields = ('first_name', 'last_name', 'phone', 'birthdate', 'fav_maker', 'budget', 'purpose', 'status')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone': 'Mobile Number',
            'author': 'Post Author',
            'birthdate': 'Date of Birth',
            'fav_maker': 'Favourite Car Maker',
            'budget': 'Financial Budget',
            'purpose': 'Purpose',
            'status': 'Post Status',
            }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'mb-3 form-control'}),
            'birthdate': forms.DateInput(attrs={'class': 'mb-3 form-control'}),
            'fav_maker': forms.Select(attrs={'class': 'mb-3 form-control'}),
            'budget': forms.NumberInput(attrs={'class': 'mb-3 form-control'}),
            'purpose': forms.TextInput(attrs={'class': 'mb-3 form-control'}),
        }


class EditApplicationForm(forms.ModelForm):
    """
    Defines the model for editing the application form
    """
    class Meta:
        model = Consultation
        fields = ('budget', 'purpose')
        labels = {
            'budget': 'Budget',
            'purpose': 'Purpose',
            }
