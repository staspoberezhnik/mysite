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

    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.email = self.cleaned_data['email']
    #
    #     if commit:
    #         user.save()
    #     return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'telephone',
            'birth_date',
            'country',
            'photo',

        ]

    # def save(self,commit=True):
    #     profile = super(ProfileForm, self).save(commit=False)
    #     profile.telephone = self.cleaned_data['telephone']
    #     profile.birth_date = self.cleaned_data['birth_date']
    #     profile.country = self.cleaned_data['country']
    #     profile.photo = self.cleaned_data['photo']
    #
    #     if commit:
    #         profile.save()
    #         return profile


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = {
            'password',
            'email',
            'first_name',
            'last_name',
        }