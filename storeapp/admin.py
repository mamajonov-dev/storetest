from django.contrib import admin

# Register your models here.


from .models import *


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    list_display_links = ('title', )

@admin.register(BasketModel)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'product', 'quantity')
    list_display_links = ('user', )


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'basket', 'user','create_order', 'status')
    list_display_links = ('basket', )


@admin.register(OrderCategory)
class OrderCategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
