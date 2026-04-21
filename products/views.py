from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import RentalForm
from .models import Product


# 🏠 Главная страница (товары)
def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


# 🛒 Добавить в корзину
def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])

    cart.append(product_id)

    request.session['cart'] = cart

    return redirect('cart')


# 🛍 Корзина
def cart_view(request):
    cart = request.session.get('cart', [])

    products = Product.objects.filter(id__in=cart)

    return render(request, 'cart.html', {'products': products})


# 📩 Форма аренды
def rental_request(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            send_mail(
                'Новая заявка на аренду AssiaMall',
                f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}',
                'saminuraazhykanova@gmail.com',
                ['saminuraazhykanova@gmail.com'],
                fail_silently=False,
            )

            return render(request, 'success.html')
    else:
        form = RentalForm()

    return render(request, 'rental_form.html', {'form': form})