from django.urls import path
from .views import signup_view, signin_view, signout_view, index_view, add_view, decrypt_view

urlpatterns = [
    path('signup', signup_view, name='sign_up'),
    path('signin', signin_view, name='sign_in'),
    path('signout', signout_view, name='sign_out'),
    path('', index_view, name='index'),
    path('add', add_view, name='add_password'),
    path('decrypt/<int:app_id>', decrypt_view, name='decrypt_password')
]
