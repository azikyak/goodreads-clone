from django.utils import timezone
from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

from users.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    isbn = models.CharField(max_length=20)
    cover_picture = models.ImageField(default='def_cover_pic.jpeg')
    
    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    bio = models.TextField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.book.title} by {self.author.first_name} {self.author.last_name}"
    


class BookReview(models.Model):
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    comment = models.TextField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ["-created_time"]
    
    def __str__(self):
        return f"{self.stars} stars for {self.book.title} by {self.user.username}"