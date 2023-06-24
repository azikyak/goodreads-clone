from django.db import models

from users.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    isbn = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title