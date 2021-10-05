from django import forms
from django.contrib.auth.models import User

class UserForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']