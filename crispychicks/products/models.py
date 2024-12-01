from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class custom_manager(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset()

    def rolls(self):
        return super().get_queryset().filter(product_category_id=1)
     
    def korean_popcorn(self):
        return super().get_queryset().filter(product_category_id=2)
    
    def value_lunch_special(self):
        return super().get_queryset().filter(product_category_id=3)
    
    def wednesday_offer(self):
        return super().get_queryset().filter(product_category_id=4)
    
    def chicken_bucket(self):
        return super().get_queryset().filter(product_category_id=5)
    
    def box_meals(self):
        return super().get_queryset().filter(product_category_id=6)
    
    def burger(self):
        return super().get_queryset().filter(product_category_id=7)
    
    def soft_drinks(self):
        return super().get_queryset().filter(product_category_id=8)
    
    def rice_bowl(self):
        return super().get_queryset().filter(product_category_id=9)



class Categories(models.Model):
    def __str__(self):
        return self.category_name

    category_name = models.CharField(max_length=110,null=False)
    category_slug = AutoSlugField(populate_from='category_name',unique=True)
    

class Product(models.Model):

    product_name =  models.CharField(max_length=100,null=False)
    product_description = models.TextField(default="product description")
    product_price = models.PositiveIntegerField(default=0)
    product_image = models.ImageField(upload_to="products/")
    product_category = models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True)
    cust_manager = custom_manager()


    
