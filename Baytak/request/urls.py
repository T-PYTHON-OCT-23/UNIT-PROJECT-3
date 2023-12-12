from django.urls import path
from . import views
app_name = "request"

urlpatterns = [
    path('<service_id>/add/', views.addRequest, name="addRequest"),
    path('', views.veiwRequest, name="veiwRequest"),
    path('all/request/', views.allRequest , name ="allRequest"),
    path('confirm/Request/<service_id>', views.confirmRequest , name="confirmRequest"),
    path('delete/Request/<requset_id>', views.deleteRequest , name="deleteRequest")
    
    
]