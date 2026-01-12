from django.contrib import admin
from .models import Category,Product,Image


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'parent', 'is_active']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'created_at']

@admin.register(Image)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'product']