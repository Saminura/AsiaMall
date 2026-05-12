from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255, default="Product")
    description = models.TextField(default="No description")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.title