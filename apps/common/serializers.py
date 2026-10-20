from rest_framework import serializers
from .models import Item

class AddNumbersSerializer(serializers.Serializer):
    n1 = serializers.FloatField(required=True, error_messages={"required": "Please provide 'n1'."})
    n2 = serializers.FloatField(required=True, error_messages={"required": "Please provide 'n2'."})

    def validate(self, attrs):
        n1 = attrs["n1"]
        n2 = attrs["n2"]

        total = int(n1) + int(n2)

        return {
            "n1": int(n1),
            "n2": int(n2),
            "result": total,
        }


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "item_id",
            "item_code",
            "item_name",
            "uom",
            "unit_price",
            "is_active",
            "created_at",
        ]
