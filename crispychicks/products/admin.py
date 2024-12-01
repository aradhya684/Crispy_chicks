from django.contrib import admin
from .models import Product, Categories #import every model

# Register your models here.


# admin.site.register(Product) #write this for every model 



class productinfo(admin.ModelAdmin):
    list_display =['id','product_name','product_price','product_category'] #predefined variable do not write any other variable name
    

admin.site.register(Product,productinfo) 


class productcategory(admin.ModelAdmin):
    list_display = ['id','category_name','category_slug']

admin.site.register(Categories,productcategory)

#orm method is used to filter products use python shell

