from django import forms


class CustomerInfoChange(forms.Form):
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

    email = forms.EmailField(
        max_length=50,
        widget=forms.EmailInput(
          attrs={
                "id": "email",
                "placeholder": "e-mail",
                "class": "form-control"
            }
        ),
        required = False
    )
