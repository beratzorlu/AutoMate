from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Consultation
from .forms import ApplicationForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consultations'] = self.queryset
        return context


class AddApplications(generic.CreateView):
    """
    Class-based view for adding a new consultation application
    """
    model = Consultation
    template_name = 'consultation/add_application.html'
    form_class = ApplicationForm
    success_url = reverse_lazy('consultation-list')

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        return super(AddApplications, self).form_valid(form)
