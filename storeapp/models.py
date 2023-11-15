from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.TextField(verbose_name='Manzil', blank=True, null=True, default='None')
    image = models.ImageField(verbose_name='Rasm', blank=True, null=True, upload_to='users/')


class CategoryModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Kategoriya nomi')
    slug = models.CharField(max_length=100, verbose_name='Kategoriya slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class ProductModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Produkt nomi', unique=True)
    price = models.DecimalField(default=0, verbose_name='Produkt narxi', max_digits=12, decimal_places=2)
    about = models.TextField(verbose_name='Produkt haqida')
    image = models.ImageField(upload_to='products/', verbose_name='Parodukt rasmi')

    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, verbose_name='Kategoriyasi')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produktlar'


class BasketModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    creates_timestemp = models.DateTimeField(auto_now_add=True)
    order = models.BooleanField(default=False, blank=True, null=True, verbose_name='zakaz')

    class Meta:
        verbose_name = 'Karzinka'
        verbose_name_plural = 'Karzinkalar'

    def sum(self):
        return self.product.price * self.quantity


class OrderCategory(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Order kategoriyasi'
        verbose_name_plural = 'Order kategoriyalari'
    def __str__(self):
        return self.name

class OrderModel(models.Model):
    basket = models.ForeignKey(BasketModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_order = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.ForeignKey(OrderCategory, on_delete=models.CASCADE, blank=True, null=True)


    class Meta:
        verbose_name = 'Zakaz'
        verbose_name_plural = 'Zakazlar'
