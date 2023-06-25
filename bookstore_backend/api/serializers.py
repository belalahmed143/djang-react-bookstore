from store.models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class WriterSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = Writer
        fields = '__all__'

    def get_category(self, obj):
        return CategorySerializer(obj.category).data

class BookStoreSerializer(serializers.ModelSerializer):
    categoris = serializers.SerializerMethodField()
    writer = serializers.SerializerMethodField()
    class Meta:
        model = BookStore
        fields = '__all__'

    def get_categoris(self, obj):
        return CategorySerializer(obj.categoris).data

    def get_writer(self, obj):
        return WriterSerializer(obj.writer).data

class CartItemSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = '__all__'

    def get_book(self, obj):
        return BookStoreSerializer(obj.book).data


class OrderSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_books(self, obj):
        return CartItemSerializer(obj.books.all(), many=True).data
        
    def get_total(self, obj):
        return obj.get_total()
