from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm


class UserRegistrForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': "Введите имя"
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        "placeholder": "Введите фамилию"

    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        "placeholder": "Введите имя пользователя"
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4',
        "placeholder": "Введите адрес эл. почты"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        "placeholder": "Введите пароль"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        "placeholder": "Подтвердите пароль"
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfile_Form(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4",
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
    }), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'readonly': True
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4',

    }))

    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Россия, Москва, ул. Мира, дом 6',
        'class': 'form-control py-4',
    }), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email', 'address')
