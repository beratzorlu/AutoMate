# Generated by Django 3.2.18 on 2023-05-11 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0008_remove_consultation_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='fav_maker',
            field=models.CharField(choices=[('Select Car Maker', 'Select Car Maker'), ('Acura', 'Acura'), ('Alfa Romeo', 'Alfa Romeo'), ('Aston Martin', 'Aston Martin'), ('Audi', 'Audi'), ('Bentley', 'Bentley'), ('BMW', 'BMW'), ('Buick', 'Buick'), ('Cadillac', 'Cadillac'), ('Chevrolet', 'Chevrolet'), ('Chrysler', 'Chrysler'), ('Dodge', 'Dodge'), ('Ferrari', 'Ferrari'), ('Fiat', 'Fiat'), ('Ford', 'Ford'), ('Genesis', 'Genesis'), ('GMC', 'GMC'), ('Honda', 'Honda'), ('Hyundai', 'Hyundai'), ('Infiniti', 'Infiniti'), ('Jaguar', 'Jaguar'), ('Jeep', 'Jeep'), ('Kia', 'Kia'), ('Lamborghini', 'Lamborghini'), ('Land Rover', 'Land Rover'), ('Lexus', 'Lexus'), ('Lincoln', 'Lincoln'), ('Lotus', 'Lotus'), ('Maserati', 'Maserati'), ('Mazda', 'Mazda'), ('McLaren', 'McLaren'), ('Mercedes-Benz', 'Mercedes-Benz'), ('Mini', 'Mini'), ('Mitsubishi', 'Mitsubishi'), ('Nissan', 'Nissan'), ('Pagani', 'Pagani'), ('Porsche', 'Porsche'), ('Ram', 'Ram'), ('Rolls-Royce', 'Rolls-Royce'), ('Subaru', 'Subaru'), ('Tesla', 'Tesla'), ('Toyota', 'Toyota'), ('Volkswagen', 'Volkswagen'), ('Volvo', 'Volvo')], default='default', max_length=16),
        ),
    ]