from . import views
from django.urls import path

urlpatterns = [
    path('apply/', views.ConsultationList.as_view(), name="consultation-list"),
    path('application-form/', views.AddApplications.as_view(), name="application-form"),  # noqa
    path('edit/<int:pk>', views.EditApplications.as_view(), name="edit-application"),  # noqa
    path('remove/<int:pk>', views.RemoveApplications.as_view(), name="remove-application"),  # noqa
]
