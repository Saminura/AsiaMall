from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(verbose_name="Product Name", max_length=255)
    image = models.ImageField(verbose_name="Product Image", upload_to="products/")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name="Category Name", max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"