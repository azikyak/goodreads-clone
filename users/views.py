from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from .models import User
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

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("landing_page")

class ProfileView(View):
    def get(self, request, username):
        return render(
            request,
            'registration/profile.html',
            {
                "user":request.user
            }
        )

class ProfileEditView(View):
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
            files=request.FILES
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