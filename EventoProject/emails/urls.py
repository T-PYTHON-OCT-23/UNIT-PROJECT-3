from django.urls import path
from . import views
app_name = "emails"


urlpatterns = [
    path("book/", views.the_bill_view , name="the_bill_view")

]
