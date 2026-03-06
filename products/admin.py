from django.contrib import admin
from .models import Product, Category, SubCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "subcategory")
    search_fields = ("name",)
    list_filter = ("subcategory",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    search_fields = ("name",)
    list_filter = ("category",)    
