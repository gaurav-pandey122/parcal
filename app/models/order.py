from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from app.models.store import Store
from app.utils.helper import generate_code
from app.utils.order import ORDER_STATUS, WEIGHT_CHOICES


class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="orders")
    consignment_id = models.CharField(max_length=100, unique=True, null=True)
    order_id = models.CharField(max_length=255, null=True, blank=True)

    order_date = models.DateField(auto_now_add=True)
    customer_name = models.CharField(max_length=100, null=False, blank=False)
    customer_phone = PhoneNumberField(null=False, blank=False, region="NP")
    customer_secondary_phone = PhoneNumberField(region="NP", null=True, blank=True)
    customer_address = models.TextField(null=False, blank=False)

    total_weight = models.CharField(
        max_length=100, choices=WEIGHT_CHOICES, default="pending"
    )
    quantity = models.PositiveIntegerField(null=False, blank=False, default=1)
    amount = models.FloatField(null=False, blank=False, default=0.0)

    special_instructions = models.TextField(null=True, blank=True)
    item_description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=ORDER_STATUS, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.consignment_id

    def generate_consignment_id(self):
        while True:
            code = generate_code("DI")
            if not Order.objects.filter(consignment_id=code).exists():
                self.consignment_id = code
                break
        return self.consignment_id

    def save(self, *args, **kwargs):
        if not self.consignment_id:
            self.consignment_id = self.generate_consignment_id()

        return super(Order, self).save(*args, **kwargs)
