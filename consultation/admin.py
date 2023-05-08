from django.contrib import admin
from .models import Consultation
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Consultation)
class AdminConsultation(admin.ModelAdmin):
    actions = ['application_approval']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    list_display = ('first_name', 'last_name', 'email', 'birthdate', 'fav_maker', 'budget', 'purpose', 'created_on', 'updated_on', 'status', 'approved')
    list_filter = ('created_on', 'approved', 'email', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'status')

    def application_approval(self, request, queryset):
        queryset.update(approved=True)