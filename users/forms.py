from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()


    # username = forms.CharField(
    #     label = 'Имя пользователя',
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                   'class': 'search-box-1',
    #                                   'placeholder': 'Введите ваше имя пользователя'}))
    # password = forms.CharField(
    #     label = 'Пароль',
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                       'class': 'search-box-1',
    #                                       'placeholder': 'Введите ваш пароль'}))
    class Meta:
        model = User
        fields = ['username', 'password']