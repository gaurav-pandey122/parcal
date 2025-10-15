from rest_framework import serializers

from app.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "store",
            "consignment_id",
            "order_id",
            "order_date",
            "customer_name",
            "customer_phone",
            "customer_secondary_phone",
            "customer_address",
            "total_weight",
            "quantity",
            "amount",
            "special_instructions",
            "item_description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "order_date", "created_at", "updated_at"]

    def validate_amount(self, value):
        if value < 0:
            raise serializers.ValidationError("Amount cannot be negative.")
        return value

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be at least 1.")
        return value
