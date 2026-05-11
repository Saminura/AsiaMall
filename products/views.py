from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Product, Order, OrderItem


# 🏠 Главная страница
def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


# 🛒 Корзина
def cart_view(request):
    cart = request.session.get('cart', {})

    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)

    cart_items = []
    total_price = 0

    for product in products:
        quantity = cart[str(product.id)]
        item_total = product.price * quantity

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total
        })

        total_price += item_total

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


# ➕ добавить в корзину
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart

    return redirect('cart')


# 🧹 очистка корзины
def clear_cart(request):
    request.session['cart'] = {}
    return redirect('cart')


# 🧾 создать заказ
def create_order(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('cart')

    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)

    order = Order.objects.create(total_price=0)

    total_price = 0

    for product in products:
        quantity = cart[str(product.id)]
        item_total = product.price * quantity

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=product.price
        )

        total_price += item_total

    order.total_price = total_price
    order.save()

    request.session['cart'] = {}

    return redirect('order_detail', order_id=order.id)


# 📦 просмотр заказа
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order.html', {'order': order})
from django.core.mail import send_mail

def rental_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        send_mail(
            'Новая заявка на аренду',
            f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}',
            'from@example.com',
            ['your_email@example.com'],
            fail_silently=False,
        )

        return redirect('home')

    return render(request, 'rental_form.html')