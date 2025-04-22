from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("", views.PrivateUser.as_view()),
    # "me" should be upper than <str:username>
    # if not, me considered as username
    path("me", views.Me.as_view()),
    path("change-password", views.ChangePassword.as_view()),
    path("log-in", views.LogIn.as_view()),  # using cookies and password
    path("log-out", views.LogOut.as_view()),
    path("token-login", obtain_auth_token),  # using auth tokens
    path("jwt-login", views.JWTLogIn.as_view()),  # using jwt
    path("@<str:username>", views.PublicUser.as_view()),
]
