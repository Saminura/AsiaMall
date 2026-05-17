from django.urls import path
from .views import product_list, add_to_cart, cart_view

urlpatterns = [
    path('', product_list),
    path('add/<int:product_id>/', add_to_cart),
    path('cart/', cart_view),
]
