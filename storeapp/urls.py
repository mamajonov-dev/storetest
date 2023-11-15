from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('products/', products, name='products'),
    path('products/<int:page_number>/', products, name='paginator'),

    path('order/', order_page, name='order'),
    path('create-order/', order_careate, name='order_create'),
    path('orders/', orders, name='orders'),
    path('success/', success, name='success'),
    path('email_verification/', email_verification, name='email_verification'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),
    path('delete-account/<int:pk>/', delete_user, name='delete_user'),

    path('category/<str:slug>/', products, name='category'),
    path('register/', userregistration, name='register'),
    path('basket/add/<int:product_id>', basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', delete_basket, name='delete_basket')



]
