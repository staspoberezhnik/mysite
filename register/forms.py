from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


class ProfileForm(forms.ModelForm):
    telephone = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Profile
        fields = [
            'telephone',
            'birth_date',
            'country',
            'photo',

        ]


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = {
            'password',
            'email',
            'first_name',
            'last_name',
        }