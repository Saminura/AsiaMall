from django.db import models

class Product(models.Model):
    name = models.CharField(verbose_name="Product Name", max_length=255)
    image = models.ImageField(verbose_name="Product Image", upload_to="products/")
    subcategory = models.ForeignKey("SubCategory", verbose_name="Sub Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(verbose_name="Category Name", max_length=255)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(verbose_name="Sub Category Name", max_length=255)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)    

    def __str__(self):
        return self.name

