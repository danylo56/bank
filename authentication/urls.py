from django.urls import path
from authentication.views import SignUpView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name="sign_up"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
]
