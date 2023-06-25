from django.urls import path
from .views import *

urlpatterns = [
    path('', home , name='home'),
    path('book-detail/<pk>', book_detail, name='book-detail'),
    path('add-to-cart/<pk>', add_to_cart, name='add-to-cart'),
    path('cart-summary', cart_summary, name='cart-summary'),
    path('quantity-increment/<pk>', quantity_increment, name='quantity-increment'),
    path('quantity_decrement/<pk>', quantity_decrement, name='quantity-decrement'),
    path('remove_from_cart/<pk>', remove_from_cart, name='remove_from_cart'),
]