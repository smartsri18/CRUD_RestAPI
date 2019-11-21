from .views import LoginView, RegisterUsersView
from django.urls import path

urlpatterns = [
    path("login/",LoginView.as_view(),name="auth-login"),
    path('register/', RegisterUsersView.as_view(), name="auth-register")
]
