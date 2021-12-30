from django import forms
from django.db.models import fields
from django.forms import widgets

from app.models import *
from django.utils.translation import gettext_lazy as g

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput}
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','profile_pic']
    