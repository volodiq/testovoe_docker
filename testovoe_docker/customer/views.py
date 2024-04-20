from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import CustomerInfoChange
from .models import CustomerProfile


class ProfileView(FormView):
    """Личный кабинет заказчика"""
    template_name = "customer/profile.html"
    form_class = CustomerInfoChange
    success_url = reverse_lazy("customer:profile")

    def form_valid(self, form):
        cd = form.cleaned_data
        # Изменение полей профиля
        profile = CustomerProfile.objects.get(user=self.request.user)
        profile.phone = cd["phone"]
        print(profile.phone)
        profile.save()
        # Изменение полей пользователя
        user = self.request.user
        user.first_name = cd["first_name"]
        user.last_name = cd["last_name"]
        user.email = cd["email"]
        user.save()
        return super().form_valid(form)

    def get_initial(self):
        profile = CustomerProfile.objects.get(user=self.request.user)
        phone = profile.phone
        first_name = self.request.user.first_name
        last_name = self.request.user.last_name
        email = self.request.user.email
        return {
            "phone": phone,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
        }
