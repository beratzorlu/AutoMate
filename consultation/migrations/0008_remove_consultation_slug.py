# Generated by Django 3.2.18 on 2023-05-10 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0007_remove_consultation_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation',
            name='slug',
        ),
    ]
