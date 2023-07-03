from django.shortcuts import render, redirect
from .utils import encrypt, decrypt
from .models import AppPassword
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='sign_in')
def index_view(request):
    user = request.user
    index_page = 'index.html'
    app_list = AppPassword.objects.filter(user=user)
    return render(request, index_page, context={'app_list': app_list})


@login_required(login_url='sign_in')
def add_view(request):
    user = request.user
    app_name = request.POST['appname']
    password = request.POST['password']
    AppPassword.objects.create(
        app_name=app_name,
        password=encrypt(password),
        user=user
    )
    messages.success(request, "Added successfully.")
    return redirect('index')


@login_required(login_url='sign_in')
def decrypt_view(request, app_id):
    user = request.user
    index_page = 'index.html'
    app_list = AppPassword.objects.filter(user=user)
    password_obj = AppPassword.objects.get(pk=app_id)
    app_name = password_obj.app_name
    decrypted_password = decrypt(password_obj.password)
    return render(request, index_page, context={'app_name': app_name,
                                                'decrypted_password': decrypted_password,
                                                'app_list': app_list})


def signup_view(request):
    signup_page = 'sign_up.html'
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username).exists():
            messages.error(request, "username already taken. please try with different username.")
            return render(request, signup_page)
        if password1 != password2:
            messages.error(request, "Passwords didn't match!! Please try again.")
            return render(request, signup_page)
        else:
            User.objects.create_user(username=username, password=password1)
            messages.info(request, 'Account created successfully, Please login with your credentials.')
            return redirect('sign_in')

    return render(request, signup_page)


def signin_view(request):
    signin_page = 'sign_in.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials, Please try again..")
            return render(request, signin_page)
    return render(request, signin_page)


def signout_view(request):
    logout(request)
    return redirect('sign_in')
