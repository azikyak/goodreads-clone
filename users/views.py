from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from users.models import User, Friends, FriendsRequest
from .forms import RegisterForm, UserUpdateForm

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        
        return render(
            request,
            'registration/register.html',
            {
                "register_form":register_form,
            }
        )
    
    def post(self, request):
        register_form = RegisterForm(data=request.POST)
        
        if register_form.is_valid():
            register_form.save()
            return redirect('users:login')
        else:
            return render(
                request,
                'registration/register.html',
                {
                    "register_form":register_form,
                }
            )


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        return render(
            request,
            'registration/login.html',
            {
                "login_form":login_form,
            }
        )
    
    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home_page')
        else:
            return render(
                request,
                'registration/login.html',
                {
                    "login_form":login_form,
                }
            )

class LogoutView(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        return redirect("landing_page")

class ProfileView(View, LoginRequiredMixin):
    def get(self, request, username):
        return render(
            request,
            'registration/profile.html',
            {
                "user":request.user
            }
        )

class ProfileEditView(View, LoginRequiredMixin):
    def get(self, request, username):
        update_form = UserUpdateForm(instance=request.user)
        return render(
            request,
            'registration/profile-edit.html',
            {
                "update_form":update_form,
            }
        )
        
    def post(self, request, username):
        update_form = UserUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES,
        )
        if update_form.is_valid():
            update_form.save()
            return redirect('users:profile',username=username)
        else:
            return render(
                request,
                'registration/profile-edit.html',
                {
                    "update_form":update_form,
                }
            )
            
            
class AllUsersView(View):
    def get(self, request):
        users = User.objects.all().order_by("pk")
        return render(request, 'registration/users.html',
                      {
                          "users":users,
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
        return redirect("home_page")
    
class RejectFriendRequest(LoginRequiredMixin, View):
    def post(self, request, pk):
        from_user = User.objects.get(pk=pk)
        FriendsRequest.objects.get(from_user=from_user,to_user=request.user).rejected()
        return redirect("home_page")