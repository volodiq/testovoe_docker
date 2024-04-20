from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import redirect

from customer.models import CustomerProfile
from executor.models import ExecutorProfile


class UserRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/registration.html"
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        cd = form.cleaned_data
        user = User.objects.create_user(username=cd["username"], password=cd["password2"])
        # Создание профилей
        CustomerProfile.objects.create(user=user)
        ExecutorProfile.objects.create(user=user)
        return redirect(self.success_url)


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "accounts/login.html"
