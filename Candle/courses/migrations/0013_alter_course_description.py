# Generated by Django 5.0 on 2023-12-12 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_alter_course_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(),
        ),
    ]
