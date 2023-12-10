from . import views
from django.urls import path


app_name = 'services'


urlpatterns = [
    path('',views.show_services_view,name='show_services_view'),
    path('add/',views.add_service_view,name='add_service_view'),
]