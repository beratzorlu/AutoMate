from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
from consultation.cars import CAR_MAKER_CHOICES


STATUS = ((0, "Draft"), (1, "Published"))


class Consultation(models.Model):
    """
    Class-based model for consultation applications
    """
    first_name = models.CharField(max_length=200, unique=False)
    last_name = models.CharField(max_length=200, unique=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="consultation_application")
    birthdate = models.DateField()
    phone = PhoneNumberField(null=False, blank=False, unique=False)
    fav_maker = models.CharField(
        max_length=16, choices=CAR_MAKER_CHOICES, default='default')
    budget = models.PositiveIntegerField(validators=[MaxValueValidator(999999)])
    purpose = models.CharField(max_length=200, unique=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default="0")
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f'Application by {self.author}.'
    
    def get_absolute_url(self):
        return reverse('consultation-list', args={self.slug})

