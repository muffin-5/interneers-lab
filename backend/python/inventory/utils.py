from rest_framework.response import Response
from rest_framework import status


def error_response(message, errors=None, status_code=status.HTTP_400_BAD_REQUEST):
    return Response(
        {
            "status": "error",
            "message": message,
            "errors": errors,
        },
        status=status_code,
    )


def success_response(data, status_code=status.HTTP_200_OK):
    return Response(
        {
            "status": "success",
            "data": data,
        },
        status=status_code,
    )
