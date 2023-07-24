from django.shortcuts import render

from book.models import BookReview

def LandingPageView(request):
    return render(request,'landing.html')

def HomePageView(request):
    reviews = BookReview.objects.all()
    return render(request,'home.html',
                  {
                    "reviews":reviews,
                  })