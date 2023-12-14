from django.db import models

# Create your models here.

class Contact(models.Model):
    status_choices = models.TextChoices("status_choices", ["Unread", "Read", "Replied"])

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=status_choices.choices, default='Unread')

    def __str__(self):
        return self.subject
