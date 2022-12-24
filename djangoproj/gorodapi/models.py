from django.db import models
# Create your models here.


class Books(models.Model):
    Name = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    Price = models.IntegerField(default=300)
    ImageURL = models.CharField(max_length=200, null=True)
    Discount = models.IntegerField(default=0)


class Users(models.Model):
    Name = models.CharField(max_length=25)
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Cart = models.IntegerField(default=0)
    Bookmarks = models.IntegerField(default=0)


class CartBooks(models.Model):
    Book = models.ForeignKey(Books, on_delete=models.CASCADE)
    User = models.ForeignKey(Users, on_delete=models.CASCADE)


class WishBooks(models.Model):
    Book = models.ForeignKey(Books, on_delete=models.CASCADE)
    User = models.ForeignKey(Users, on_delete=models.CASCADE)


class Collections(models.Model):
    Name = models.CharField(max_length=30)
    Books = models.ManyToManyField(Books)
