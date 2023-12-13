from django.urls import path
from . import views

app_name = "Consultations"

urlpatterns = [
    path('add/<user_id>', views.consultation_views, name="consultation_views"),
    path('add/request/', views.add_consultation_request_view, name="add_consultation_request_view"),
    path('myRequest/', views.consultation_request_view, name="consultation_request_view")
]

