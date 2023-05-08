from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Consultation
from django.views import generic, View
from django.urls import reverse_lazy

# Create your views here.


class ConsultationList(generic.ListView):
    """
    Class-based list view of Consultation model
    """
    model = Consultation
    queryset = Consultation.objects.filter(status=1).order_by('-created_on')
    template_name = 'consultation/consultation-list.html'
    paginate_by = 6
