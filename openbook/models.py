from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE


# Create your models here.
class User(AbstractUser):
    pass



class Book(models.Model):
    name = models.CharField(max_length=25)
    author = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    # user = models.CharField(max_length=25)

    def __str__(self):
        return self.name



class lend(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,null=True, related_name="lendby")
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.book.name} lended by {self.user.username}"




# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username


# class HomeBook(models.Model):
