from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path

from .views import LandingPageView, HomePageView

urlpatterns = [
    path('',LandingPageView, name="landing_page"),
    path('home/', HomePageView, name="home_page"),
    path('admin/', admin.site.urls),
    path('users/', include("users.urls")),
    path('books/', include("book.urls")),
    path('friends/', include("friends.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

