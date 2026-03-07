from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=500)
    category = serializers.CharField(max_length=100)
    price = serializers.FloatField()
    brand = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField()

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be a non-negative number.")
        return value

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Quantity must be a non-negative integer."
            )
        return value

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value
