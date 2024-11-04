from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone

from carts.models import Cart
from goods.models import Products

def cart(request):
    return render(request, 'carts/cart_main.html')

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
        messages.success(request, 'Товар добавлен в корзину.')
    else:
        messages.warning(request, 'Для добавления товара в корзину вам необходимо войти в систему.')
        return redirect(reverse('user:login'))  
    
    return redirect(request.META['HTTP_REFERER'])

def cart_change(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'increase':
            cart.quantity += 1
        elif action == 'decrease' and cart.quantity > 1:
            cart.quantity -= 1
        
        cart.save()
    
    return redirect(request.META['HTTP_REFERER'])


def cart_remove(request, cart_id):
    
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])