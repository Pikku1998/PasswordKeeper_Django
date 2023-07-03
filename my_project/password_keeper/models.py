from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class AppPassword(models.Model):
    app_name = models.CharField(max_length=100)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
