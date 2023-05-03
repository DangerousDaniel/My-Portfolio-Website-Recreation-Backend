"""
    Project Name: My Portfolio Website Recreation
    Authors: Daniel Cox
    Created Date: April 21, 2023
    Last Updated: April 26, 2023
    Description: This is the class for category views.
    Notes:
    Resources: 
 """

from ..models import Category
from ..serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def category_all(request, format=None):
    if request.method == 'GET':
        categories = Category.objects.all()
        categorySerializer = CategorySerializer(categories, many=True)
        return Response(categorySerializer.data)