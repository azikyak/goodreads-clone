from django.urls import path
from friends.views import   (
    AddFriendsView, 
    AcceptFriendRequest, 
    RejectFriendRequest,
    FriendsView,
    RemoveFriendList,
)

app_name = "friends"
urlpatterns = [
    path('', FriendsView.as_view(), name="friends"),
    path('add/<int:pk>/', AddFriendsView.as_view(), name="add-friend"),
    path('accept/<int:pk>/', AcceptFriendRequest.as_view(), name="accept_friend_request"),
    path('reject/<int:pk>/', RejectFriendRequest.as_view(), name="reject_friend_request"),
    path('remove/<int:pk>/', RemoveFriendList.as_view(), name="remove_friend_list"),
    
]
