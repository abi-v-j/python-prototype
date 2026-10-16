from rest_framework import serializers


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


class AddItemSerializer(serializers.Serializer):
    item_code = serializers.CharField(required=True, error_messages={"required": "Please provide 'item_code'."})
    item_name = serializers.CharField(required=True, error_messages={"required": "Please provide 'item_name'."})
    unit_price = serializers.DecimalField(max_digits=12, decimal_places=2, required=True, error_messages={"required": "Please provide 'unit_price'."})

    def validate(self, attrs):
        item_code = attrs["item_code"]
        item_name = attrs["item_name"]
        unit_price = attrs["unit_price"]

        return {
            "item_code": item_code,
            "item_name": item_name,
            "unit_price": unit_price,
        }
       
