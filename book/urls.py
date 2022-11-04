from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('<int:id>/comment/', add_comment_to_book, name='add_comment_to_book')
]
