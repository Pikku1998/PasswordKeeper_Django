from django.shortcuts import render, redirect
from .utils import encrypt, decrypt
from .models import AppPassword
from django.contrib import messages


def index_view(request):
    index_page = 'index.html'
    app_list = AppPassword.objects.all()
    return render(request, index_page, context={'app_list': app_list})


def add_view(request):
    app_name = request.POST['appname']
    password = request.POST['password']
    AppPassword.objects.create(
        app_name=app_name,
        password=encrypt(password)
    )
    messages.success(request, "Added successfully.")
    return redirect('index')


def decrypt_view(request, app_id):
    index_page = 'index.html'
    app_list = AppPassword.objects.all()
    password_obj = AppPassword.objects.get(pk=app_id)
    app_name = password_obj.app_name
    decrypted_password = decrypt(password_obj.password)
    return render(request, index_page, context={'app_name': app_name,
                                                'decrypted_password': decrypted_password,
                                                'app_list': app_list})


def signup_view(request):
    return render(request, 'sign_up.html')


def signin_view(request):
    return render(request, 'sign_in.html')


def signout_view(request):
    pass
