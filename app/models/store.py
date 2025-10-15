from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class StoreQuerySet(models.QuerySet):
    def for_user(self, user):
        return self.filter(user=user)


class Store(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    phone = PhoneNumberField(blank=False, null=False, region="NP")
    secondary_phone = PhoneNumberField(blank=False, null=False, region="NP")
    email = models.EmailField()
    address = models.CharField(max_length=255, blank=False, null=False)
    location = models.CharField(max_length=100, blank=False, null=False)
    contact_person = models.CharField(max_length=255, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stores")

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = StoreQuerySet.as_manager()

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
