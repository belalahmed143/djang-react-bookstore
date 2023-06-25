from django.urls import path
from .views import *

urlpatterns = [
    # apiurl
    path('book-store/', BookStoreListView.as_view()),
    path('book-detail/<pk>/', BookStoreDetailView.as_view()),
    path('add-to-cart/', AddToCartView.as_view()),
    path('cart-summary/',CartSummaryApiView.as_view()),
]