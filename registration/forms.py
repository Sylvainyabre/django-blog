from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import Profile, CustomUser


class CustomUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','first_name','last_name',)


class UserUpdateForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ['email','first_name','last_name',]


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ('user',)



