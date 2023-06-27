from django.db import models


class AppPassword(models.Model):
    app_name = models.CharField(max_length=100)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
