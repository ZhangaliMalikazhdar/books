from django.shortcuts import render, get_object_or_404, redirect

from book.forms import CommentForm
from book.models import Book


def index():
    return "works"


def add_comment_to_book(request, pk):
    if request.method == "POST":
        user = request.user
        beet = get_object_or_404(Book, pk=id)
        form = CommentForm(request.POST, instance=beet)
        if form.is_valid():
            form.save()
            return redirect('book:book-detail', beet.id)
    else:
        form = CommentForm()
    return render(request, 'book/add_comment_to_book.html', {'form': form})
