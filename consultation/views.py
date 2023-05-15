from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Consultation
from .forms import ApplicationForm, EditApplicationForm


class ConsultationList(generic.ListView):
    """
    Class-based list view of Consultation model
    """
    model = Consultation
    template_name = 'consultation/consultation-list.html'

    def get_queryset(self):
        return Consultation.objects.filter(status=1).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consultations'] = self.get_queryset()
        return context


class AddApplications(LoginRequiredMixin, generic.CreateView):
    """
    Class-based view for adding a new consultation application
    """
    model = Consultation
    template_name = 'consultation/add_application.html'
    form_class = ApplicationForm
    success_url = reverse_lazy('consultation-list')

    def get_queryset(self, *args, **kwargs):
        return Consultation.objects.filter(id=self.kwargs['pk'])

    def dispatch(self, request, *args, **kwargs):
        if Consultation.objects.filter(author=request.user).exists():
            messages.warning(request, "Sorry, you already submitted an application.")  # noqa
            return redirect('consultation-list')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        messages.success(self.request, 'Success! Your application has been submitted.')  # noqa
        return super(AddApplications, self).form_valid(form)


class EditApplications(LoginRequiredMixin, generic.UpdateView):
    """
    Class-based view for editing an existing consultation application
    """
    model = Consultation
    template_name = 'consultation/edit_application.html'
    form_class = EditApplicationForm

    def get(self, request, *args, **kwargs):
        consultation = self.get_object()
        if self.request.user == consultation.author or self.request.user.is_superuser:  # noqa
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def get_queryset(self, *args, **kwargs):
        return Consultation.objects.filter(id=self.kwargs['pk'])

    def form_valid(self, form):
        consultationObject = self.get_object()
        consultation = form.save(commit=False)
        if self.request.user == consultation.author or self.request.user.is_superuser:  # noqa
            consultation.save()
            messages.success(self.request, 'Success! Your changes to your application have been saved.')  # noqa
            return redirect(reverse("consultation-list"))
        else:
            messages.warning(self.request, 'You are not authorized to edit this page.')  # noqa
            return redirect(reverse("consultation-list"))


class RemoveApplications(LoginRequiredMixin, generic.DeleteView):
    """
    Class-based view for deleting an existing consultation application
    """

    model = Consultation
    template_name = 'consultation/remove_application.html'
    success_url = reverse_lazy('consultation-list')

    def test_func(self):
        consultation = self.get_object()
        return self.request.user == consultation.author or self.request.user.is_superuser  # noqa

    def get_queryset(self, *args, **kwargs):
        return Consultation.objects.filter(id=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        consultation = self.get_object()
        if self.request.user == consultation.author or self.request.user.is_superuser:  # noqa
            messages.success(self.request, 'Your application has been successfully removed.')  # noqa
            return super(RemoveApplications, self).delete(request, *args, **kwargs)  # noqa
        else:
            messages.warning(self.request, 'You are not authorized to access this page.')  # noqa
            return HttpResponseForbidden()
