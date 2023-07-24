from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    book_author_staff = models.BooleanField(default=False)
    profile_picture = models.ImageField(default='def_pic.jpeg')
    country = models.CharField(max_length=200,default='')
    city = models.CharField(max_length=200,default='')
