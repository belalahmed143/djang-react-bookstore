from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):    
    books = BookStore.objects.all().order_by('?')
    context={
        'books':books,

    }    
    return render(request, 'index.html',context)

def book_detail(request, pk):
    book = BookStore.objects.get(pk=pk)
    another_book =BookStore.objects.all().exclude(pk=pk)[:12]
    
    context ={
        'book':book,
        'another_book':another_book
    }
    return render(request, 'book-details.html',context)
        
@login_required
def add_to_cart(request,pk):
    book = get_object_or_404(BookStore, pk=pk)
    cart_item, created = CartItem.objects.get_or_create(book=book,user=request.user,ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.books.filter(book__pk=book.pk).exists():
           cart_item.quantity += 1
           cart_item.save()
           messages.success(request,'this book quantity update')
           return redirect('book-detail',pk=book.pk)
        else:
            order.books.add(cart_item)
            messages.info(request,'this book was add to cart')
            return redirect('book-detail',pk=book.pk)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.books.add(cart_item)
        messages.info(request,'this book was add to cart')
        return redirect('book-detail',pk=book.pk)

@login_required
def cart_summary(request):
    try:
        order = Order.objects.get(user=request.user, ordered=False)

        context ={
            'order':order
        }
        return render(request, 'cart-summary.html',context)
    except ObjectDoesNotExist:
        messages.info(request,'your cart is empty')
        return redirect('/')

@login_required
def quantity_increment(request,pk):
    book = get_object_or_404(BookStore, pk=pk)
    cart_item, created = CartItem.objects.get_or_create(book=book,user=request.user,ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.books.filter(book__pk=book.pk).exists():
           cart_item.quantity += 1
           cart_item.save()
           messages.success(request,'this book quantity update')
           return redirect('cart-summary')
    else:
        return redirect('cart-summary')

@login_required
def quantity_decrement(request,pk):
    book = get_object_or_404(BookStore, pk=pk)
    cart_item, created = CartItem.objects.get_or_create(book=book,user=request.user,ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.books.filter(book__pk=book.pk).exists():
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
                messages.info(request,'this book quantity update')
                return redirect('cart-summary')
            else:
                cart_item.delete()
                messages.info(request,'this book was delete')
                return redirect('cart-summary')
        else:
            return redirect('cart-summary')
    else:
        return redirect('cart-summary')

@login_required
def remove_from_cart(request,pk):
    book = get_object_or_404(BookStore, pk=pk)
    cart_item, created = CartItem.objects.get_or_create(book=book,user=request.user,ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.books.filter(book__pk=book.pk).exists():
            cart_item.delete()
            messages.info(request,'this book was delete')
            return redirect('cart-summary')
        else:
            messages.info(request,'this book was not your cart')
            return redirect('cart-summary')
    else:
        return redirect('cart-summary')

