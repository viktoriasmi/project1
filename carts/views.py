from django.shortcuts import redirect, render

from carts.models import Cart
from goods.models import Products

def cart(request):
    return render(request, 'carts/cart.html')

def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META['HTTP_REFERER'])

def cart_change(request, cart_id):
    if request.method == 'POST':
        action = request.POST.get('action')

        cart = Cart.objects.get(id=cart_id)

        if action == 'increase':
            cart.quantity += 1
            cart.save()
        elif action == 'decrease' and cart.quantity > 1:  
            cart.quantity -= 1
            cart.save()

    return redirect(request.META['HTTP_REFERER'])



def cart_remove(request, cart_id):
    
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])