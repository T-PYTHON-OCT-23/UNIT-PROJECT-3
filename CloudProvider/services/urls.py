from . import views
from django.urls import path


app_name = 'services'


urlpatterns = [
    path('',views.show_services_view,name='show_services_view'),
    path('add/',views.add_service_view,name='add_service_view'),
    path('detils/<service_id>/',views.service_detils_view,name='service_detils_view'),
    path('request/<serivce_id>/',views.request_service_view,name='request_service_view'),
    path('request/history',views.view_services_i_reqeust_view,name='view_services_i_reqeust_view'),
    
]