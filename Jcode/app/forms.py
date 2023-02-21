from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Member


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ( 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ['id','user', 'created', 'updated']
