from django.urls import path
from . import views


urlpatterns =[
    
path('',views.ProductListView.as_view(),name="productspage"),
path("search/",views.search,name="search"),
path('new-chicken-rolls/',views.rolls,name="rollpage"),
path('korean-popcorn/',views.korean_popcorn,name="kpoppage"),
path('value-lunch-specials/',views.value_lunch_special,name="vlspage"),
path('wednesday-offer/',views.wednesday_offer,name="wopage"),
path('chicken-buckets/',views.chicken_bucket,name="cbpage"),
path('box-meals/',views.box_meals,name="bmpage"),
path('burgers/',views.burger,name="burgerpage"),
path('beverages-desserts/',views.soft_drinks,name="softdrinkpage"),
path('rice-bowlz/',views.rice_bowl,name="rbpage")

]


