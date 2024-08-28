from django.contrib import admin
from django.urls import path,include

from login import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/user/register2/", views.UserViewRegister.as_view(),name="register2"),
    path("login/user/register/", views.UserVeterinariaViewRegister.as_view(),name="register"),
    path("login/token/", TokenObtainPairView.as_view(),name = "get_token"),
    path("login/token/refresh/", TokenRefreshView.as_view(), name = "refresh"),
    path("login-auth/", include("rest_framework.urls")),
    path("mascota/",include("mascota.urls")),
    path("api-notes/", include("api.urls")),
]