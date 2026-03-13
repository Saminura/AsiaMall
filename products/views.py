from rest_framework import viewsets, mixins
from .models import Product, Category, SubCategory
from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer   


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer    

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from .utils import send_order_email

@login_required
def create_order(request):
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        quantity = int(request.POST.get("quantity", 1))
        
        order = Order.objects.create(
            user=request.user,
            product_name=product_name,
            quantity=quantity
        )
        
        send_order_email(request.user.email, order)
        return render(request, "products/order_success.html", {"order": order})
    
    return render(request, "products/create_order.html")    