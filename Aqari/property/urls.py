from django.urls import path
from . import views

app_name = "property"

urlpatterns = [path("add/",views.add_property_view,name='add_property_view'),
               path("update/<property_id>/",views.update_property_view,name='update_property_view'),
               path('delete/<property_id>/',views.delete_property_view,name="delete_property_view"),
               path('home/',views.property_home_view,name='property_home_view'),
               path('detail/<property_id>/',views.detail_property_view,name='detail_property_view'),
               path('rental/<property_id>/',views.rental_property_view,name='rental_property_view'),
               path('sale/<property_id>/',views.sale_property_view,name='sale_property_view'), 
               path('rent/',views.rental_property_list_view, name='rental_property_list_view'),
               path('sale/',views.sale_property_list_view, name='sale_property_list_view'),
               path('sold/',views.sold_properties_view,name='sold_properties_view'),
               path('purchases/',views.purchases_properties_view,name='purchases_properties_view'),
               path('rented/',views.rented_properties_view,name='rented_properties_view'),
               path('rented/by/you',views.rented_by_you_view,name='rented_by_you_view'),
               path('customers/',views.property_customers_view,name='property_customers_view'),
               path("search/", views.search_results_view, name="search_results_view"),
               path('comment/add/<property_id>/',views.add_comment_view,name="add_comment_view"),
               path('delete/comment/<comment_id>/',views.delete_comment_view,name="delete_comment_view"),
               path('comments/<comment_id>/',views.comment_detail_view,name='comment_detail_view'),
               path('comments/',views.comment_view,name='comment_view'),
               path('rent/view/',views.rent_view,name='rent_view'),
               path('rent/<rent_id>/',views.rent_detail_view,name='rent_detail_view'),
               path('delete/rent/<rent_id>/',views.delete_rent_view,name="delete_rent_view"),
               path('sales/view/',views.sale_view,name='sale_view'),
               path('sales/<sale_id>/',views.sale_detail_view,name='sale_detail_view'),
               path('delete/sales/<sale_id>/',views.delete_sale_view,name="delete_sale_view"),
               
               ]