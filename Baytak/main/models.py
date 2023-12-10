from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.TextField()
    requestType = models.TextChoices("RequestType", ["Suggestions", "Complaints", "Inquiry", "Report"])
    evaluation = models.TextChoices("Evaluation", ["Very Good" , "Good" , "Unsatisfactory"])

