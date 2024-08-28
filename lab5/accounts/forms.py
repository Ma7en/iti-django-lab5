from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        # fields = ["username", "email", "password1", "password2"]
        fields = ["username", "email"]


class UserRegistrationForm2(forms.Form):
    username = forms.CharField(required=True)
    # class Meta:
    #     model = User
    #     fields = ["username", "email", "password1", "password2"]
