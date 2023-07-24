from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from users.models import User
from users.forms import RegisterForm, UserUpdateForm
from friends.models import Friends, FriendsRequest

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
                "user":request.user,
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
        friends = any
        friend_requested = any
        if request.user.is_authenticated:
            friends = Friends.objects.friends(request.user)
            friend_requested = FriendsRequest.objects.filter(from_user=request.user)
        return render(request, 'registration/users.html',
                      {
                          "users":users,
                          "friends":friends,
                          "friend_requested":friend_requested,
                      })