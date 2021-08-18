from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Book,Order,Customer


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class NewBook(ModelForm):
    class Meta:
        model=Book
        fields='__all__'
        exclude=['reating']

class EditOrderForm(ModelForm):
    class Meta:
        model=Order
        fields=['pay_stattus','pay_method','stattus']


class EditProfileForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']
