from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm)
from .forms import RegistrationForm, ProfileForm, EditProfileForm
from .models import Profile
from django.shortcuts import get_object_or_404
# Create your views here.


def log_in(request):
    context = {
        'form': AuthenticationForm(),
    }

    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('post:home')
        else:
            context = {
                'error': 'user not found',
            }
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)


def log_out(request):
    auth.logout(request)
    return redirect('post:home')


def register(request):

    if request.POST:
        newuser_form = RegistrationForm(request.POST or None)
        profile_form = ProfileForm(request.POST or None, request.FILES or None)

        if newuser_form.is_valid() and profile_form.is_valid():

            newuser_form.save()
            newuser = auth.authenticate(
                username=newuser_form.cleaned_data['username'],
                password=newuser_form.cleaned_data['password1'], )

            auth.login(request, newuser)
            profile = profile_form.save(commit=False)
            profile.user = User.objects.get(id=newuser.id)
            profile.save()
            return redirect('post:home')
        else:
            return redirect('post:users_list')
    else:
        context = {
            'user_form': RegistrationForm(),
            'profile_form': ProfileForm(),
        }
        return render(request, 'register.html', context)


def view_profile(request, id):
    user_instance = get_object_or_404(User, id=id)
    username = None
    can_edit = None
    if request.user.is_staff or\
            request.user.is_superuser or\
            request.user.is_authenticated:
        username = auth.get_user(request).username

    if user_instance.id == request.user.id:
        can_edit = True

    context = {
        'user': user_instance,
        'can_edit': can_edit,
        'username': username,
    }

    return render(request, 'profile.html', context)


def edit_profile(request, id):
    user_instance = get_object_or_404(User, id=id)
    profile_instance = user_instance.profile
    user = request.user

    if request.user.is_staff or\
            request.user.is_superuser or\
            request.user.is_authenticated:
        username = auth.get_user(request).username

        if user_instance.id == user.pk:
            if request.POST:

                user_form = EditProfileForm(request.POST, instance=user_instance)
                profile_form = ProfileForm(request.POST or None,
                                           request.FILES or None,
                                           instance=profile_instance)
                if user_form.is_valid() and profile_form.is_valid():
                    user_form.save()
                    profile_form.save()

                    return redirect('auth:view_profile', id=request.user.id)
                else:
                    return redirect('auth:edit_profile', id=request.user.id)
            else:
                user_form = EditProfileForm(instance=request.user)
                profile_form = ProfileForm(instance=request.user.profile)
                context = {
                    'user_form': user_form,
                    'profile_form': profile_form,
                    'username': username,
                }
            return render(request, 'edit_profile.html', context)
        else:
            return redirect('auth:my_profile')
    else:
        return redirect('post:home')


def password_change(request, id):
    user_instance = get_object_or_404(User, id=id)
    user = request.user
    username = None
    if request.user.is_staff or\
            request.user.is_superuser or\
            request.user.is_authenticated:
        username = auth.get_user(request).username

        if user_instance.id == user.pk:

            if request.POST:
                form = PasswordChangeForm(data=request.POST, user=request.user)

                if form.is_valid():
                    form.save()
                    update_session_auth_hash(request, form.user)
                    return redirect('auth:view_profile', id=request.user.id)

            else:
                form = PasswordChangeForm(user=request.user)
                context = {
                    'form': form,
                    'username': username
                }
                return render(request, 'change_password.html', context)
        else:
            return redirect('auth:my_profile')
    else:
        return redirect('post:home')


def my_profile(request):
    user_instance = get_object_or_404(User, id=auth.get_user(request).id)

    username = None
    can_edit = None
    if request.user.is_staff or\
            request.user.is_superuser or\
            request.user.is_authenticated:
        username = auth.get_user(request).username

    if user_instance.id == request.user.id:
        can_edit = True

    context = {
        'user': user_instance,
        'can_edit': can_edit,
        'username': username,
    }

    return render(request, 'profile.html', context)