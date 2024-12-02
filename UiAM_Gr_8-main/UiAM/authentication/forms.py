from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class EdytujUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name','last_name']

class EdytujUserPhone(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone']