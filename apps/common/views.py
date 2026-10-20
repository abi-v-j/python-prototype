from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AddNumbersSerializer, ItemSerializer
from .models import Item


@api_view(["GET"])
def checking(request):
    return Response(
        {
            "success": True,
            "message": "Checking API is running",
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
def add_two_numbers(request):
   
    serializer = AddNumbersSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        return Response(
            {
                "status": "success",
                "n1": data["n1"],
                "n2": data["n2"],
                "result": data["result"],
                "message": f"Sum calculated successfully: {data['n1']} + {data['n2']} = {data['result']}",
            },
            status=status.HTTP_200_OK,
        )
    return Response(
        {
            "status": "error",
            "errors": serializer.errors,
            "hint": "Please supply 'n1' and 'n2' in JSON format, e.g. {'n1': 10, 'n2': 20}",
        },
        status=status.HTTP_400_BAD_REQUEST,
    )




@api_view(["GET", "POST"])
def insert_item_orm(request):
  
    if request.method == "POST":
        item_code = request.data.get("item_code")
        item_name = request.data.get("item_name")
        unit_price = request.data.get("unit_price", 0)
        uom = request.data.get("uom", "NOS")

        if not item_code or not item_name:
            return Response(
                {"error": "Both 'item_code' and 'item_name' are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

      
        new_item = Item.objects.create(
            item_code=item_code,
            item_name=item_name,
            unit_price=unit_price,
            uom=uom,
        )

        serializer = ItemSerializer(new_item)
        return Response(
            {
                "status": "success",
                "message": "Item inserted successfully using Django ORM (.objects.create)",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

    elif request.method == "GET":
        items = Item.objects.all().order_by("item_id")
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

