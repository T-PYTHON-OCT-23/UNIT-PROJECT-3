from django.urls import path
from . import views
app_name = "emails"


urlpatterns = [
    path("contact_us/", views.contact_us_view , name="contact_us_view"),
    path("book/", views.the_bill_view , name="the_bill_view")

]
