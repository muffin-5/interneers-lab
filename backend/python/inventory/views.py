from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .in_memory_store import products_db, current_id

@api_view(['POST'])
def create_product(request):
    global current_id
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        product = serializer.validated_data
        product['id'] = current_id
        products_db[current_id] = product
        current_id += 1
        return Response(product, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_products(request):
    return Response(list(products_db.values()), status=status.HTTP_200_OK)

@api_view(['GET'])
def get_product(request, pk):
    product = products_db.get(pk)
    if not product:
        return Response({"error": "Product not found"},
        status = status.HTTP_404_NOT_FOUND,
        )
    return Response(product, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_product(request, pk):
    product = products_db.get(pk)
    if not product:
        return Response(
            {"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        updated = serializer.validated_data
        updated['id'] = pk
        products_db[pk] = updated
        return Response(updated, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_product(request, pk):
    if pk not in products_db:
        return Response(
            {"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    del products_db[pk]
    return Response(status=status.HTTP_204_NO_CONTENT)


