# Generated by Django 5.0 on 2023-12-07 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0004_alter_car_fuel_type_alter_car_transmission_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="car",
            name="rental_company",
        ),
    ]
