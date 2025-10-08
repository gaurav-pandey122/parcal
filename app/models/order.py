from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from app.models.store import Store
from app.utils.order import WEIGHT_CHOICES


class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="orders")
    consignment_id = models.CharField(
        max_length=100,
        unique=True,
    )

    order_date = models.DateField(auto_now_add=True)
    customer_name = models.CharField(max_length=100, null=False, blank=False)
    customer_phone = PhoneNumberField(null=False, blank=False, region="NP")
    customer_secondary_phone = PhoneNumberField(region="NP")
    customer_address = models.TextField(null=False, blank=False)

    total_weight = models.CharField(
        max_length=100, choices=WEIGHT_CHOICES, default="pending"
    )
    quantity = models.PositiveIntegerField(null=False, blank=False, default=1)
    amount = models.FloatField(null=False, blank=False, default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.consignment_id
