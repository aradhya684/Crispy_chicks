from django.shortcuts import render,HttpResponseRedirect
from .models import cart,CartItem,Order,OrderItem
from products.models import Product
from .forms import orderform
import uuid
from django.core.mail import send_mail
from crispychicks.settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required
import razorpay
from django.views.decorators.csrf import csrf_exempt




@login_required(login_url = "/login")
def add_to_cart(request,productID):
 
    currentUser = request.user
    cart_obj,created = cart.objects.get_or_create(user = currentUser) #name of varible and model should not be same
    request.session["cart_id"]=cart_obj.id
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
    cart_items = user_cart.cartitem_set.all() #here cartitem is our model name it is converted into lowercase from uppercase
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
            order=Order.objects.create(order_id = uuid.uuid4().hex,
                                       user = request.user,
                                       address_line_1 = form.cleaned_data["address_line_1"],
                                       address_line_2 = form.cleaned_data["address_line_2"],
                                       city = form.cleaned_data['city'], 
                                       state = form.cleaned_data['state'], 
                                       pincode = form.cleaned_data['pincode'], 
                                       phone_no = form.cleaned_data['phone_no'])
            
            cart_id=request.session.get("cart_id")
            Cart=cart.objects.get(id= cart_id)
            cartitems=Cart.cartitem_set.all()



            for i in cartitems:
                OrderItem.objects.create(order=order,
                                         quantity=i.quantity,
                                         products=i.products)

    return HttpResponseRedirect("/cart/payment/"+order.order_id)



@login_required(login_url="/login")
def payment(request,orderId):
    order=Order.objects.get(order_id=orderId)
    orderitems=order.orderitem_set.all()
    total=0
    for orderitem in orderitems:
        total+=orderitem.quantity*orderitem.products.product_price
        
    currentUser = request.user
    user_cart = cart.objects.get(user = currentUser)
    cart_items = user_cart.cartitem_set.all() #here cartitem is our model name it is converted into lowercase from uppercase
    total_price = 0
    for i in cart_items:
        total_price += i.quantity*i.products.product_price
        
    final_price = total_price
    gst = round(final_price*0.05,2)
    final_after_gst = final_price+gst

    client=razorpay.Client(auth=("rzp_test_9OqmIDeq85cvr3","LVkt6Cs9VskcAarHG1ryJNdr"))
    data = { "amount": total*100, "currency": "INR", "receipt": orderId }
    payment=client.order.create(data=data)
    return render(request,"payment.html",{"payment":payment,"total_price":final_price,"gst":gst,"final_after_gst":final_after_gst})


@csrf_exempt
def paymentSuccess(request,orderId):
    razorpay_response={
        "razorpay_payment_id":request.POST.get("razorpay_payment_id"),
        "razorpay_order_id":request.POST.get("razorpay_order_id"),
        "razorpay_signature":request.POST.get("razorpay_signature")
    }
    client=razorpay.Client(auth=("rzp_test_9OqmIDeq85cvr3","LVkt6Cs9VskcAarHG1ryJNdr"))
    payment_check=client.utility.verify_payment_signature(razorpay_response)
    if payment_check:
        print("order is paid")
        order=Order.objects.get(order_id=orderId)
        order.paid=True
        order.save()
        send_mail(f"[{order.order_id} placed]",
                  "Order placed successfully...",
                   EMAIL_HOST_USER,["gauriambole123@gmail.com"],
                  fail_silently=False)
        
        
        currentUser=request.user
        Cart=cart.objects.get(user=currentUser)
        cartitems=Cart.cartitem_set.all()
        total=0
        for cartitem in cartitems:
             cartitem.delete()

    return render(request,"success.html",{"orderitems":order.orderitem_set.all()})




