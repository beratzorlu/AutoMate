from .models import Consultation
from crispy_forms.helper import FormHelper
from django.forms.widgets import DateInput
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django import forms


class ApplicationForm(forms.ModelForm):
    """
    Defines the model for the application form
    """
    phone = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='IE'))

    class Meta:
        model = Consultation
        fields = ('first_name', 'last_name', 'phone', 'birthdate', 'fav_maker', 'budget', 'purpose')  # noqa
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone': 'Mobile Number',
            'author': 'Post Author',
            'birthdate': 'Date of Birth',
            'fav_maker': 'Favourite Car Maker',
            'budget': 'Financial Budget (€)',
            'purpose': 'Purpose',
            'status': 'Post Status',
            }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'mb-3 form-control'
                }),
            'last_name': forms.TextInput(attrs={
                'class': 'mb-3 form-control'
                }),
            'birthdate': forms.DateInput(attrs={
                'placeholder': 'DD-MM-YYYY',
                'class': 'mb-3 form-control',
                'type': 'date',
                }),
            'fav_maker': forms.Select(attrs={
                'class': 'mb-3 form-control'
                }),
            'budget': forms.NumberInput(attrs={
                'class': 'mb-3 form-control',
                'placeholder': 'e.g. 40000'
                }),
            'purpose': forms.TextInput(attrs={
                'class': 'mb-3 form-control',
                'placeholder': 'e.g. Daily driver, family SUV'
                }),
        }


class EditApplicationForm(forms.ModelForm):
    """
    Defines the model for editing the application form
    """
    class Meta:
        model = Consultation
        fields = ('budget', 'purpose', 'fav_maker')
        labels = {
            'budget': 'Budget',
            'purpose': 'Purpose',
            'fav_maker': 'Favourite Car Maker',
            }
