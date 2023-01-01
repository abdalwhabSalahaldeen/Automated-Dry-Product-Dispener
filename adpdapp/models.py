from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.urls import reverse

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    def __str__(self):
        return self.user.username

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="products")
    selling_price = models.DecimalField(verbose_name="price",decimal_places=4,max_digits=50)
    description = models.TextField()
    Quantity=models.PositiveIntegerField(default=1000)
    number=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images/")

    def __str__(self):
        return self.product.title


class Cart(models.Model):
    total = models.DecimalField(default=0,decimal_places=4,max_digits=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart: " + str(self.id)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.DecimalField(default=0,decimal_places=4,max_digits=50)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(default=0,decimal_places=4,max_digits=50)

    def __str__(self):
        return "Cart: " + str(self.cart.id) + " CartProduct: " + str(self.id)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    total = models.DecimalField(default=0,decimal_places=4,max_digits=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Order: " + str(self.id)
