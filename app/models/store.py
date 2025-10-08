from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class Store(models.Model):
    name = models.CharField(max_length=255)
    phone = PhoneNumberField(blank=False, null=False, region="NP")
    secondary_phone = PhoneNumberField(blank=False, null=False, region="NP")
    email = models.EmailField()
    address = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=100, blank=True)
    contact_person = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stores")

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["phone"]),
        ]
        verbose_name = "Store"
        verbose_name_plural = "Stores"

    def __str__(self):
        return self.name
