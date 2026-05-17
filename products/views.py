from django.shortcuts import render, redirect
from .models import Product, CartItem


def product_list(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/')


def cart_view(request):
    cart_items = CartItem.objects.all()
    total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })
