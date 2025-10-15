from django import forms
from phonenumber_field.formfields import PhoneNumberField

from app.models import Order


class OrderForm(forms.ModelForm):
    customer_phone = PhoneNumberField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
        region="NP",
    )
    customer_secondary_phone = PhoneNumberField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False,
        region="NP",
    )

    class Meta:
        model = Order
        fields = [
            "store",
            "order_id",
            "customer_name",
            "customer_phone",
            "customer_secondary_phone",
            "customer_address",
            "total_weight",
            "quantity",
            "amount",
            "item_description",
            "special_instructions",
        ]
        widgets = {
            "store": forms.Select(attrs={"class": "form-control"}),
            "order_id": forms.TextInput(attrs={"class": "form-control"}),
            "customer_name": forms.TextInput(attrs={"class": "form-control"}),
            "customer_address": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),
            "total_weight": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
            "amount": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.01"}
            ),
            "special_instructions": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),
            "item_description": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if self.errors.get(field_name):
                print(field_name, self.errors.get(field_name))

                existing_classes = field.widget.attrs.get("class", "")
                field.widget.attrs["class"] = f"{existing_classes} is-invalid".strip()
