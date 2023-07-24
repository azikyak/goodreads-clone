from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from friends.models import Friends, FriendsRequest
from users.models import User


class FriendsView(LoginRequiredMixin, View):
    def get(self, request):
        friends = Friends.objects.friends(request.user)
        friend_requested_users = FriendsRequest.objects.filter(to_user=request.user)
        return render(request,"friends/friends.html",
                      {
                          "friends":friends,
                          "friend_requested_users":friend_requested_users,
                      })


class AddFriendsView(LoginRequiredMixin, View):
    def post(self, request, pk):
        to_user = get_object_or_404(User,pk=pk)
        Friends.objects.add_friend(from_user=request.user,to_user=to_user)
        ls = Friends.objects.friends(request.user)
        print(*ls)
        return redirect("users:all-users")

class AcceptFriendRequest(LoginRequiredMixin, View):
    def post(self, request, pk):
        from_user = User.objects.get(pk=pk)
        FriendsRequest.objects.get(from_user=from_user,to_user=request.user).accept()
        return redirect("friends:friends")

class CancelFriendRequest(LoginRequiredMixin, View):
    def post(self, request, pk):
        to_user = User.objects.get(pk=pk)
        FriendsRequest.objects.get(from_user=request.user,to_user=to_user).cancel()
        return redirect("friends:friends")

class RejectFriendRequest(LoginRequiredMixin, View):
    def post(self, request, pk):
        from_user = User.objects.get(pk=pk)
        FriendsRequest.objects.get(from_user=from_user,to_user=request.user).rejected()
        return redirect("friends:friends")