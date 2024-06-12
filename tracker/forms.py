from django import forms
from .models import Watchlist, Item
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class WatchlistForm(forms.ModelForm):
    class Meta:
        model = Watchlist
        fields = ['name', 'description']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'url']
