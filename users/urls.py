from django.urls import path

from users.views import (
    RegisterView, 
    LoginView, 
    LogoutView, 
    ProfileView, 
    ProfileEditView, 
    AllUsersView,
    RegisterAPIView,
    LoginAPIView,
)

app_name = "users"
urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name="register_api"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('all/', AllUsersView.as_view(), name="all-users"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profile/<str:username>/', ProfileView.as_view(), name="profile"),
    path('profile/<str:username>/edit/', ProfileEditView.as_view(), name="profile-edit"),
]
