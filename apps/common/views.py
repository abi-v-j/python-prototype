from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def checking(request):
    return Response(
        {
            "success": True,
            "message": "Checking API is running",
        },
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
def add_two_numbers(request):
    try:
        result = 23 + 67
        return Response(
            {
                "success": True,
                "message": "Numbers added successfully",
                "result": result
            },
            status=status.HTTP_200_OK
        )
    except (ValueError, TypeError):
        return Response(
            {
                "success": False,
                "message": "Invalid input. Please provide valid numbers."
            },
            status=status.HTTP_400_BAD_REQUEST
        )