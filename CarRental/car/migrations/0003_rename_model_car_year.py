# Generated by Django 5.0 on 2023-12-07 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0002_rentalcompany_rename_year_car_pags_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="car",
            old_name="model",
            new_name="year",
        ),
    ]
