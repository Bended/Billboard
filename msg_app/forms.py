from django.contrib.auth.models import User
from django import forms

from .models import Messages

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


# class PostForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fields = ('title', 'text', 'author')