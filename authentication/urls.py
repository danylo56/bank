from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from authentication.views import SignUpView

urlpatterns = [
    path('sign-up', SignUpView.as_view(), name="sign_up"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
]
