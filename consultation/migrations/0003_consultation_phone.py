# Generated by Django 3.2.18 on 2023-05-09 14:59

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0002_alter_consultation_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]