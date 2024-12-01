from django.urls import path
from . import views

urlpatterns =[

path("",views.show_cart,name = "showcart"),
path("add-to-cart/<int:productID>/",views.add_to_cart,name = "addtocart"),
path("update-cart/<int:pk>/",views.update_cartitem,name = "update_cart_item"),
path("delete-cart/<int:pk>/",views.delete_cartitem,name = "delete_cart_item"),
path("checkout/",views.checkout,name = "checkout")

]


