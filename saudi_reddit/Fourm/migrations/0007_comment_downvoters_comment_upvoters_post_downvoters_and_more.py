# Generated by Django 4.2.7 on 2023-12-10 12:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Fourm', '0006_alter_post_content_alter_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='downvoters',
            field=models.ManyToManyField(blank=True, related_name='downvoted_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='upvoters',
            field=models.ManyToManyField(blank=True, related_name='upvoted_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='downvoters',
            field=models.ManyToManyField(blank=True, related_name='downvoted_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='upvoters',
            field=models.ManyToManyField(blank=True, related_name='upvoted_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
