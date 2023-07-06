from django.forms import ModelForm
from book.models import BookReview

class BookReviewForm(ModelForm):
    class Meta:
        model = BookReview
        fields = ( 'comment', 'stars' )
        