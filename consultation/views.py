from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Consultation
from .forms import ApplicationForm, EditApplicationForm

# Create your views here.


class ConsultationList(generic.ListView):
    """
    Class-based list view of Consultation model
    """
    model = Consultation
    template_name = 'consultation/consultation-list.html'
    paginate_by = 6

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

    def dispatch(self, request, *args, **kwargs):
        if Consultation.objects.filter(author=request.user).exists():
            messages.warning(request, "Sorry, you already submitted an application.")
            return redirect('consultation-list')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        messages.success(self.request, 'Success! Your application has been submitted.')
        return super(AddApplications, self).form_valid(form)


class EditApplications(LoginRequiredMixin, generic.UpdateView):
    """
    Class-based view for editing an existing consultation application
    """
    model = Consultation
    template_name = 'consultation/edit_application.html'
    form_class = EditApplicationForm

    def form_valid(self, form):
        consultation = form.save(commit=False)
        consultation.save()
        messages.success(self.request, 'Success! Your changes to your application have been saved.')
        return redirect(reverse("consultation-list"), pk=consultation.pk)


class RemoveApplications(LoginRequiredMixin, generic.DeleteView):
    """
    Class-based view for deleting an existing consultation application
    """
    
    model = Consultation
    template_name = 'consultation/remove_application.html'
    success_url = reverse_lazy('consultation-list')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, 'Your application ID: %(id)s has been successfully removed.' % obj.__dict__)
        return super(RemoveApplications, self).delete(request, *args, **kwargs)


class ConsultationDetailView(View):
    """
    Class-based view of the post detail page
    """
    def get(self, request, *args, **kwargs):
        queryset = Consultation.objects.filter(status=1)
        pk = self.kwargs.get('pk')
        consultation = get_object_or_404(queryset, pk=pk)

        return render(
            request,
            "consultation-list.html",
            {
                "consultation": consultation,
            },
        )

    def post(self, request, *args, **kwargs):
        queryset = Consultation.objects.filter(status=1)
        pk = self.kwargs.get('pk')
        consultation = get_object_or_404(queryset, pk=pk)

        return render(
            request,
            "consultation-list.html",
            {
                "consultation": consultation,
            },
        )

