from django import forms
from seller.models import Bikes
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SellerForm(forms.ModelForm):
    class Meta:
        model = Bikes
        fields = "__all__"


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]


class LoginForm(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
