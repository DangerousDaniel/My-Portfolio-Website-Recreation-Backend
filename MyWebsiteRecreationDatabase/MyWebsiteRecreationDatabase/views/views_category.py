"""
    Project Name: My Portfolio Website Recreation
    Authors: Daniel Cox
    Created Date: April 21, 2023
    Last Updated: May 3, 2023
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

        jsonData = {'Categories': categorySerializer.data}
        databaseMessageJson = {'Database Message': f"Database select queries was successfully retrieved from the {Category.__name__} table."}
        
        response = [jsonData, databaseMessageJson]
        return Response(response)