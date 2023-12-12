# Generated by Django 4.1.2 on 2023-12-11 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car", "0011_alter_car_air_conditioner_alter_car_fuel_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="city",
            field=models.CharField(
                choices=[
                    ("Riyadh", "Riyadh"),
                    ("Abha", "Abha"),
                    ("Khobar", "Khobar"),
                    ("Hail", "Hail"),
                    ("Jeddah", "Jeddah"),
                ],
                default="Riyadh",
                max_length=124,
            ),
        ),
    ]
