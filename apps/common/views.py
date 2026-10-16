from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AddNumbersSerializer, AddItemSerializer



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




@api_view(["POST"])
def add_item(request):
   
    serializer = AddItemSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        return Response(
            {
                "status": "success",
                "item_code": data["item_code"],
                "item_name": data["item_name"],
                "unit_price": data["unit_price"],
                "message": f"Item added successfully: {data['item_code']} - {data['item_name']} at {data['unit_price']}",
            },
            status=status.HTTP_200_OK,
        )
    return Response(
        {
            "status": "error",
            "errors": serializer.errors,
            "hint": "Please supply 'item_code', 'item_name', and 'unit_price' in JSON format, e.g. {'item_code': 'ITEM001', 'item_name': 'Product Name', 'unit_price': 10.99}",
        },
        status=status.HTTP_400_BAD_REQUEST,
    )
