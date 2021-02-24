from django.contrib.auth.views import LogoutView
from django.urls import path
from authentication.views import SignUpView, CustomLoginView

urlpatterns = [
    path('sign-up', SignUpView.as_view(), name="sign_up"),
    path('login', CustomLoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
]
