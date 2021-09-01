from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory

from django.contrib.auth.models import User #the originl user model

from .models import Order, OrderItems

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class OrderItemsForm(ModelForm):
    class Meta:
        model = OrderItems
        fields = ['order', 'dishes', 'quantity']
