from django.shortcuts import render
from .models import Product, Categories
from django.views.generic import ListView
# from django.utils.decorators import method_decorator
# from django.contrib.admin.views.decorators import staff_member_required


class ProductListView(ListView):
    model = Product

    

def rolls(request):
    items = Product.cust_manager.rolls()
    return render(request,"products/rolls.html",{"rolls":items})

def korean_popcorn(request):
    items = Product.cust_manager.korean_popcorn()
    return render(request,"products/korean_popcorn.html",{"korean_popcorn":items})

def value_lunch_special(request):
    items = Product.cust_manager.value_lunch_special()
    return render(request,"products/value_lunch_special.html",{"value_lunch_special":items})

def wednesday_offer(request):
    items = Product.cust_manager.wednesday_offer()
    return render(request,"products/wednesday_offer.html",{"wednesday_offer":items})

def chicken_bucket(request):
    items = Product.cust_manager.chicken_bucket()
    return render(request,"products/chicken_bucket.html",{"chicken_bucket":items})

def box_meals(request):
    items = Product.cust_manager.box_meals()
    return render(request,"products/box_meals.html",{"box_meals":items})

def burger(request):
    items = Product.cust_manager.burger()
    return render(request,"products/burger.html",{"burger":items})

def soft_drinks(request):
    items = Product.cust_manager.soft_drinks()
    return render(request,"products/soft_drinks.html",{"soft_drinks":items})

def rice_bowl(request):
    items = Product.cust_manager.rice_bowl()
    return render(request,"products/rice_bowl.html",{"rice_bowl":items})

def search(request):
    keyword = request.GET.get("keyword")
    items = Product.cust_manager.all().filter(product_name__icontains = keyword)
    return render(request,"products/search.html", {"products":items})