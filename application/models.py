from django.db import models

# AbstractUser
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.


# class User(AbstractUser):
#     mobile 

class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file_path = models.FileField(upload_to='static/resources/')

    def __str__(self):
        return self.title