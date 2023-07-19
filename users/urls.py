from django.urls import path

from users.views import RegisterView, LoginView, LogoutView, ProfileView, ProfileEditView, AllUsersView, AddFriendsView, AcceptFriendRequest, RejectFriendRequest


app_name = "users"
urlpatterns = [
    path('all/', AllUsersView.as_view(), name="all-users"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profile/<str:username>/', ProfileView.as_view(), name="profile"),
    path('profile/<str:username>/edit/', ProfileEditView.as_view(), name="profile-edit"),
    path('friends/<int:pk>/', AddFriendsView.as_view(), name="add-friend"),
    path('friends/accept/<int:pk>/', AcceptFriendRequest.as_view(), name="accept_friend_request"),
    path('friends/reject/<int:pk>/', RejectFriendRequest.as_view(), name="reject_friend_request"),
]
