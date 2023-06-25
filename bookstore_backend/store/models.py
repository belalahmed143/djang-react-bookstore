from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name  = models.CharField(max_length = 150)
    parent_cate  = models.ForeignKey('self', on_delete=models.CASCADE, related_name='chaild', blank=True, null=True)

    def __str__(self):
        return self.name   

class Writer(models.Model):
    name  = models.CharField(max_length = 150)
    category  = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class BookStore(models.Model):
    name = models.CharField(max_length=100)
    categoris = models.ForeignKey(Category, on_delete=models.CASCADE)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='BookImg',default='BookImg/noimg.jpg')
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    discription = RichTextUploadingField()
    stock_quantity = models.PositiveIntegerField()

    def saving_price(self):
        return self.price  - self.discount_price

    def saving_percent(self):
        return self.saving_price() / self.price  * 100
        
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

class CartItem(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    ordered = models.BooleanField(default=False) 
    book = models.ForeignKey(BookStore, on_delete=models.CASCADE) 
    quantity = models.IntegerField(default=1) 
  
    def saving_price(self):
        return (self.book.price * self.quantity) - (self.book.discount_price * self.quantity)

    def saving_percent(self):
        return (self.saving_price()) / (self.book.price * self.quantity) * 100

    def get_subtotal(self):
        if self.book.discount_price:
            return self.book.discount_price * self.quantity
        else:
            return self.book.price * self.quantity

    def __str__(self):
        return f"{self.quantity} of {self.book.name}"

    class Meta:
        ordering = ['-id']


class Order(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    books = models.ManyToManyField(CartItem)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

   
    def __str__(self):
        return self.user.username   

    def get_total(self):
        total = 0
        for i in self.books.all():
            total += i.get_subtotal()
        return total

    class Meta:
        ordering = ['-id']