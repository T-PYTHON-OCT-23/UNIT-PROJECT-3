from django.urls import path
from . import views

app_name = "Consultations"

urlpatterns = [
    path('add/<user_id>', views.consultation_views, name="consultation_views")
]

