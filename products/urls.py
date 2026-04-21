from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('cart/', views.cart_view, name='cart'),

    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('rental/', views.rental_request, name='rental'),
]