from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import ExecutorInfoChange
from .models import ExecutorProfile


class ProfileView(FormView):
    """Личный кабинет исполнителя"""
    template_name = "executor/profile.html"
    form_class = ExecutorInfoChange
    success_url = reverse_lazy("executor:profile")

    def form_valid(self, form):
        cd = form.cleaned_data
        # Изменение полей профиля
        profile = ExecutorProfile.objects.get(user=self.request.user)
        profile.phone = cd["phone"]
        profile.experience = cd["experience"]
        profile.save()
        # Изменение полей пользователя
        user = self.request.user
        user.first_name = cd["first_name"]
        user.last_name = cd["last_name"]
        user.email = cd["email"]
        user.save()
        return super().form_valid(form)

    def get_initial(self):
        profile = ExecutorProfile.objects.get(user=self.request.user)
        phone = profile.phone
        experience = profile.experience
        first_name = self.request.user.first_name
        last_name = self.request.user.last_name
        email = self.request.user.email
        return {
            "phone": phone,
            "experience": experience,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
        }
