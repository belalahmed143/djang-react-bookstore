from django.shortcuts import render,get_object_or_404, redirect
from store.models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView,RetrieveUpdateAPIView
)
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response

class BookStoreListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BookStoreSerializer
    queryset = BookStore.objects.all()

class BookStoreDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BookStoreSerializer
    queryset = BookStore.objects.all()

class AddToCartView(APIView):
    def post(self, request, *args, **kwargs):
        id = request.data.get('id', None)
        book = get_object_or_404(BookStore, id=id)
        cart_item, created = CartItem.objects.get_or_create(book=book,user=request.user,ordered=False)
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            if order.books.filter(book__id=book.id).exists():
                cart_item.quantity += 1
                cart_item.save()
                return Response({"message": "this book quantity update"}, status=HTTP_200_OK)
            else:
                order.books.add(cart_item)
                return Response({"message": "this book was add to cart"}, status=HTTP_200_OK)
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(user=request.user, ordered_date=ordered_date)
            order.books.add(cart_item)
            return Response({"message": "this book was add to cart"}, status=HTTP_200_OK)

class CartSummaryApiView(RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            return order
        except ObjectDoesNotExist:
            raise Http404("wrong")
