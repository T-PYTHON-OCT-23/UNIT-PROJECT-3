# Generated by Django 5.0 on 2023-12-12 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_addition_time_course_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
    ]
