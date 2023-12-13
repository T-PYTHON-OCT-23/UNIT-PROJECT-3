from . import views
from django.urls import path


app_name = 'services'


urlpatterns = [
    path('',views.show_services_view,name='show_services_view'),
    path('add/',views.add_service_view,name='add_service_view'),
    path('detils/<service_id>/',views.service_detils_view,name='service_detils_view'),
    path('request/<serivce_id>/',views.request_service_view,name='request_service_view'),
    path('request/history',views.view_services_i_reqeust_view,name='view_services_i_reqeust_view'),
    path('request/<service_id>/edit/',views.edit_service_view,name='edit_service_view'),
    path('delete/request/id/<request_id>',views.delete_reqeust_view,name='delete_reqeust_view'),
    path('edit/request/<request_id>/',views.edit_request_view,name='edit_request_view'),
    path('delete/service/',views.delete_service_view,name='delete_service_view'),
    path('delete/<service_id>',views.delete_service_now_view,name='delete_service_now_view')
]