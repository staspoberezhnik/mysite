from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.


def log_in(request):
    context = {
        'form': AuthenticationForm,
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
    context = {
        'user_form': UserCreationForm,

    }
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password1'],)
            auth.login(request,newuser)
            return redirect('post:home')
        else:
            context = {
                'user_form': newuser_form
            }
    return render(request, 'register.html', context)
