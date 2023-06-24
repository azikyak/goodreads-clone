from django.shortcuts import render

def LandingPageView(request):
    return render(request,'landing.html')

def HomePageView(request):
    return render(request,'home.html')