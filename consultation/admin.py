from django.contrib import admin
from django.forms import ModelForm
from .models import Consultation


@admin.register(Consultation)
class AdminConsultation(admin.ModelAdmin):
    actions = ['application_approval']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    list_display = ('author', 'first_name', 'last_name', 'phone', 'birthdate', 'fav_maker', 'budget', 'purpose', 'created_on', 'updated_on', 'status',)
    list_filter = ('created_on', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'status')

    def application_approval(self, request, queryset):
        queryset.update(approved=True)
