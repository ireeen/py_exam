from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='products',
    )
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class ProductVersion(models.Model):
    name = models.CharField(max_length=50)
    product = models.ForeignKey(
        Product,
        related_name='product_versions',
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    client = models.ForeignKey('auth.User')
    name = models.ForeignKey(ProductVersion, related_name='carts')
    cast = models.IntegerField()

    def __int__(self):
        return self.name.id


class Order(models.Model):
    client = models.ForeignKey(
        'auth.User',
    )
    address_delivery = models.CharField(max_length=100)
    date_delivery = models.DateTimeField(auto_now=False)
    product = models.ForeignKey(Cart, related_name='orders')

    def __int__(self):
        return self.id


class Profile(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)