from rest_framework import viewsets, mixins
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer   


from django.shortcuts import render
from django.core.mail import send_mail
from .forms import RentalForm

def rental_request(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            send_mail(
                'Заявка на аренду AssiaMall',
                f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}',
                'your_email@gmail.com',
                ['admin@email.com'],
                fail_silently=False,
            )

            return render(request, 'success.html')
    else:
        form = RentalForm()

    return render(request, 'rental_form.html', {'form': form})

from django.shortcuts import render

def rental_request(request):
    return render(request, 'rental_form.html')