from django.forms import forms

from book.models import Book, Comment


class BeetsModelForm(forms.ModelForm):
    comment = forms.CharField(
        required=True,
        max_length=240,
        widget=forms.Textarea(
            attrs={
                "class": "comment form-control",
                "id": "comment-field"
            }
        )
    )

    class Meta:
        model = Book
        fields = ['comment']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']
