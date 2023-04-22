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

        categoryJson = {}
        for i in range(len(categorySerializer.data)):
            categoryData = categorySerializer.data[i]
            
            categoryJson[f'Category {i + 1}'] = categoryData

        jsonData = {'Categories': categoryJson}
        databaseMessageJson = {'Database Message': f"Database select queries was successfully retrieved from the {Category.__name__} table."}
        
        response = [jsonData, databaseMessageJson]
        return Response(response)
    
@api_view(['GET'])    
def category_detail(request, id, format=None):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist: 
        databaseMessageJson= {'Database Message': f"No data found for this id in the {Category.__name__} table."}
        response = databaseMessageJson
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        categorySerializer = CategorySerializer(category)

        jsonData = {f'Category {id}': categorySerializer.data}
        databaseMessageJson = {'Database Message': f"Database select queries was successfully retrieved from the {Category.__name__} table."}

        response = [jsonData, databaseMessageJson]
        return Response(response)
    
@api_view(['POST'])
def category_create(request, format=None):
   if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            jsonData = {f'New {Category.__name__}': serializer.data }
            databaseMessageJson = {'Database Message': f"The data has successfully created for the {Category.__name__} table."}
            
            response = [jsonData, databaseMessageJson]
            return Response(response, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def category_update(request, id, format=None):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist: 
        databaseMessageJson= {'Database Message': f"No data found for this id in the {Category.__name__} table."}
        response = databaseMessageJson
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()

            jsonData = {f'{Category.__name__} {id}': serializer.data }
            databaseMessageJson = {'Database Message': f"The data is updated for this id in {Category.__name__} table."}
            
            response = [jsonData, databaseMessageJson]
            return Response(response)
        
        databaseErrorJson = {'Database Errors': serializer.errors }
        databaseMessageJson= {'Database Message': f"Please enter the right inputs data for updating this id in {Category.__name__} table." }
        
        response = [databaseErrorJson, databaseMessageJson]
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def category_delete(request, id, format=None):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist: 
        databaseMessageJson= {'Database Message': f"No data found for this id in the {Category.__name__} table."}
        response = databaseMessageJson
        return Response(response, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == "DELETE":
        category.delete()
        databaseMessageJson= {'Database Message': f"Data has successfully delete for this id in the {Category.__name__} table."}
        response = databaseMessageJson
        return Response(response, status=status.HTTP_404_NOT_FOUND)
