from django.shortcuts import render,HttpResponseRedirect
from .models import cart,CartItem,Order
from products.models import Product
from .forms import orderform
import uuid
from django.core.mail import send_mail
# from crispychicks.settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required


@login_required(login_url = "/login")
def add_to_cart(request,productID):
 
    currentUser = request.user
    cart_obj,created = cart.objects.get_or_create(user = currentUser) #name of varible and model should not be same
    cartitem,created = CartItem.objects.get_or_create(cart = cart_obj,products = Product.cust_manager.get(id = productID))
    product_quantity = int(request.GET.get('quantity'))
    if created:
        cartitem.quantity = product_quantity
    else:
        cartitem.quantity = cartitem.quantity + product_quantity
    
    cartitem.save()
    return HttpResponseRedirect("/menu")
    
@login_required(login_url = "/login")
def show_cart(request):
    currentUser = request.user
    user_cart = cart.objects.get(user = currentUser)
    cart_items = user_cart.cartitem_set.all() #here cartitem in our model name it is converted into lowercase from uppercase
    total = 0
    for i in cart_items:
        total += i.quantity*i.products.product_price
        
    final_price = total
    gst = round(final_price*0.05,2)
    final_after_gst = final_price+gst
    return render(request,'cart.html',{"cart_items":cart_items,"total":final_price,"gst":gst,"final_after_gst":final_after_gst})

@login_required(login_url = "/login")
def update_cartitem(request,pk):
    cartitem = CartItem.objects.get(id = pk)
    cartitem.quantity = int(request.GET.get('quantity'))
    cartitem.save()
    
    return HttpResponseRedirect("/cart")

@login_required(login_url = "/login")
def delete_cartitem(request,pk):
    cartitem = CartItem.objects.get(id = pk)
    cartitem.delete()
    # send_mail(
    # "order id is 5",
    # "order placed successfully",
    # EMAIL_HOST_USER,
    # ["asaahire8@gmail.com","sadhvijadhav062@gmail.com","priyanka.vibhute@itvedant.com"],
    # fail_silently=False,)

    return HttpResponseRedirect("/cart")

@login_required(login_url = "/login")
def checkout(request):
    if request.method == 'GET':
        form = orderform()
        return render(request,"checkout.html",{"form":form})
    if request.method == 'POST':
        form = orderform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Order.objects.create(order_id = uuid.uuid4().hex,
                                  user = request.user,
                                    address_line_1 = form.cleaned_data["address_line_1"],
                                     address_line_2 = form.cleaned_data["address_line_2"],
                                      city = form.cleaned_data['city'], 
                                      state = form.cleaned_data['state'], 
                                      pincode = form.cleaned_data['pincode'], 
                                      phone_no = form.cleaned_data['phone_no'])
    return HttpResponseRedirect("/cart/checkout/")

