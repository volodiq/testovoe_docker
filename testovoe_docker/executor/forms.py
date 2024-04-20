from django import forms
from .models import ExecutorProfile


class ExecutorInfoChange(forms.Form):
    """Смена информации исполнителя"""
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "id": "firstName",
                "placeholder": "Имя",
                "class": "form-control"
            }
        )
    )

    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "id": "lastName",
                "placeholder": "Фамилия",
                "class": "form-control"
            }
        )
    )

    email = forms.EmailField(
        max_length=50,
        widget=forms.EmailInput(
            attrs={
                "id": "email",
                "placeholder": "e-mail",
                "class": "form-control"
            }
        )
    )

    experience = forms.IntegerField(
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(
            attrs={
                "min": "0",
                "max": "100",
                "type": "number",
                "id": "typeNumber",
                "class": "form-control",
                "placeholder": "0",
            },
        ),
        required=False,
    )
    phone = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "type": "tel",
                "id": "typePhone",
                "class": "form-control",
                "placeholder": "+71234567890",
            },
        ),
        required=False
    )
