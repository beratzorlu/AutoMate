# Generated by Django 3.2.18 on 2023-05-09 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0004_alter_consultation_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation',
            name='approved',
        ),
    ]
