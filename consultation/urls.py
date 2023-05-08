from . import views
from django.urls import path

urlpatterns = [
    path('consultation/', views.ConsultationList.as_view(), name="consultation-list"),
]
