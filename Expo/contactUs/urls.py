from django.urls import path
from . import views


app_name = "contactUs"


urlpatterns = [
    path('', views.contact_view, name='contact_view'),
    path('thank_you/', views.thank_you_view, name='thank_you_view'),
]
