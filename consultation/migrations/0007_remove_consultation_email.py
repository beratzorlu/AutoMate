# Generated by Django 3.2.18 on 2023-05-10 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0006_alter_consultation_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation',
            name='email',
        ),
    ]
