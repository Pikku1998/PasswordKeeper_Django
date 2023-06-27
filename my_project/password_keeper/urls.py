from django.urls import path
from .views import index_view, add_view, decrypt_view

urlpatterns = [
    path('', index_view, name='index'),
    path('add', add_view, name='add_password'),
    path('decrypt/<int:app_id>', decrypt_view, name='decrypt_password')
]
