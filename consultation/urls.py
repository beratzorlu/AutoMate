from . import views
from django.urls import path

urlpatterns = [
    path('apply/', views.ConsultationList.as_view(), name="consultation-list"),
]
