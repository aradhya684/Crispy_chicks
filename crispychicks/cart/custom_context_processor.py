from .models import cart

def cart_context_processors(request):
     cartid=request.session.get("cart_id")
     count=None
     if cartid is not None:
          Cart=cart.objects.get(id=cartid)
          count=Cart.cartitem_set.all().count()
          
     return {"count":count}
