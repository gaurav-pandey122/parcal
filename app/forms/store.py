from django import forms
from phonenumber_field.formfields import PhoneNumberField

from app.models import Store


class StoreForm(forms.ModelForm):
    location = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                "id": "locations",
                "readonly": "readonly",
            }
        ),
    )

    phone = PhoneNumberField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
        region="NP",
    )
    secondary_phone = PhoneNumberField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
        region="NP",
    )

    class Meta:
        model = Store
        fields = [
            "name",
            "phone",
            "secondary_phone",
            "email",
            "address",
            "location",
            "contact_person",
        ]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "contact_person": forms.TextInput(attrs={"class": "form-control"}),
        }
