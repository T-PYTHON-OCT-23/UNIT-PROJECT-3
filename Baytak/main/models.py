from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile

class Contact(models.Model):
    requestTypeChoices = models.TextChoices("RequestType", ["Suggestions", "Complaints", "Inquiry", "Report"])
    evaluationChoices = models.TextChoices("Evaluation", ["Very Good" , "Good" , "Unsatisfactory"])
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    requestType = models.CharField(max_length=128, choices=requestTypeChoices.choices, default="Suggestions")
    evaluation = models.CharField(max_length=128, choices=evaluationChoices.choices, default="Very Good")


