from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path

from .views import LandingPageView, HomePageView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

scheme_view = get_schema_view(
    openapi.Info(
        title="Goodreads Clone Api",
        default_version="Version 1.0",
        description="Goodreads Clone",
        terms_of_service="Nothing",
        contact=openapi.Contact(email="yusufovazimjon@gmail.com"),
        license=openapi.License(name="nothing"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
    
)


urlpatterns = [
    path('',LandingPageView, name="landing_page"),
    path('home/', HomePageView, name="home_page"),
    path('admin/', admin.site.urls),
    path('users/', include("users.urls")),
    path('books/', include("book.urls")),
    path('friends/', include("friends.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('swagger/', scheme_view.with_ui(
        'swagger', cache_timeout=0), name="swagger_swagger_ui",),
    path('redoc/', scheme_view.with_ui(
        'redoc', cache_timeout=0), name="redoc_ui",),
        
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

