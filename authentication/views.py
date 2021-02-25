from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/auth_form.html'
    extra_context = {'label': 'Sign Up'}


class CustomLoginView(LoginView):
    template_name = 'registration/auth_form.html'
    extra_context = {'label': 'Login'}
    success_url = reverse_lazy('my_cards')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
