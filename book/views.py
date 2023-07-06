from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from book.forms import BookReviewForm
from book.models import Book, BookReview


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request,"book/list.html",{"books":books})

class BookDetailView(View):
    def get(self, request, pk):
        review_form = BookReviewForm()
        book = get_object_or_404(Book,pk=pk)
        reviews = BookReview.objects.filter(book=book)
        return render(request, "book/detail.html", {
            "book":book,
            "review_form":review_form,
            "reviews":reviews,
            })
    def post(self, request, pk):
        review_form = BookReviewForm(data=request.POST)
        book = get_object_or_404(Book,pk=pk)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.book=book
            review.user=request.user
            review.save()
            return redirect("book:books-detail",pk=pk)
        else:
            return render(request, "book/detail.html", {"book":book,"review_form":review_form})