from django.contrib import admin
from django.forms import ModelForm
from .models import Consultation


@admin.register(Consultation)
class AdminConsultation(admin.ModelAdmin):
    list_display = ('author', 'first_name', 'last_name', 'phone', 'birthdate', 'fav_maker', 'budget', 'purpose', 'created_on', 'updated_on', 'status',)
    list_filter = ('author', 'created_on', 'status')
    search_fields = ('first_name', 'last_name', 'author__username')

