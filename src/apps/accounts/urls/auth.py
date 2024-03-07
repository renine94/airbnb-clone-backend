from django.urls import path

from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView
from dj_rest_auth.views import LogoutView
from dj_rest_auth.views import UserDetailsView
from rest_framework_simplejwt.views import TokenVerifyView

from ..views import auth


urlpatterns = [
    # path("register/", auth.SignupAPI.as_view(), name="signup"),
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
]
