from django.shortcuts import render

from book.models import BookReview
from users.models import FriendsRequest, Friends

def LandingPageView(request):
    return render(request,'landing.html')

def HomePageView(request):
    reviews = BookReview.objects.all()
    friend_requested_users = FriendsRequest.objects.filter(to_user=request.user)
    friends = Friends.objects.friends(user=request.user)
    print(friend_requested_users)
    return render(request,'home.html',
                  {
                      "reviews":reviews,
                      "friend_requested_users":friend_requested_users,
                      "friends":friends,
                  })