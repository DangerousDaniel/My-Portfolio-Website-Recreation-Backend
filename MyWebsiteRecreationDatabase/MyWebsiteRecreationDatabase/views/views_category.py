"""
    Project Name: My Portfolio Website Recreation
    Authors: Daniel Cox
    Created Date: April 21, 2023
    Last Updated: May 8, 2023
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

        json_data = {'categories': categorySerializer.data}

        database_error_json = {'error': False}
        database_message_json = {'message': f"Database select queries was successfully retrieved from the {Category.__name__} table."}
        database_list_json = [database_error_json, database_message_json]
        database_json = {'database': database_list_json}
        
        response_json = [json_data, database_json]
        return Response(response_json)

@api_view(['GET'])
def category_detail(request, id, format=None):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        database_error_json = {'error': True}
        database_message_json = {'message': f"No data found for this id in the {Category.__name__} table."}
        database_list_json = [database_error_json, database_message_json]
        database_json = {'database': database_list_json}
        
        response_json = [database_json]
        return Response(response_json, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        categorySerializer = CategorySerializer(category)

        json_data = {'category': categorySerializer.data}

        database_error_json = {'error': False}
        database_message_json = {'message': f"Database select queries was successfully retrieved from the {Category.__name__} table."}
        database_list_json = [database_error_json, database_message_json]
        database_json = {'database': database_list_json}
        
        response_json = [json_data, database_json]
        return Response(response_json)
