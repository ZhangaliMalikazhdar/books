from django.db import models as m
from django.db.models import Avg
from django.contrib.auth.models import User


class Genre(m.Model):
    name = m.CharField(max_length=255)


class Book(m.Model):
    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
    name = m.CharField(max_length=255)
    genre = m.ManyToManyField(Genre)
    author = m.ForeignKey('Author', on_delete=m.SET_NULL, null=True)
    date_publish = m.DateTimeField(auto_now_add=True)
    description = m.TextField()

    def __str__(self):
        return self.name


class Author(m.Model):
    full_name = m.CharField(max_length=255)


class Comment(m.Model):
    book = m.ForeignKey(Book, on_delete=m.CASCADE)
    username = m.ForeignKey(User, on_delete=m.CASCADE)
    comment = m.TextField()

    def __str__(self):
        return self.comment
