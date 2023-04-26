from ..models import Article
from ..models import Page_List
from ..models import Resource_List
from ..models import Category

from ..serializers import ArticleSerializer
from ..serializers import PageSerializer
from ..serializers import ResourceSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def article_all(request, format=None):
    if request.method == 'GET':
        articles = Article.objects.all()

        serializers = ArticleSerializer(articles, many=True)        

        articleJson = {'Articles': serializers.data}
        databaseMessageJson = {'Database Message':f"Database select query was successfully retrieved from the {Article.__name__} table." }

        responseJson = [articleJson, databaseMessageJson]
        return Response(responseJson)


@api_view(['GET'])
def article_all_quick_view(request, category_id_input, offset_num=0, limit_num=10, format=None):
    try:
        category = Category.objects.get(pk=category_id_input)
    except Category.DoesNotExist:
        databaseMessageJson= {'Database Message': f"No data found for this id in the {Category.__name__} table."}
        response = databaseMessageJson
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        articles = Article.objects.filter(category_id=category_id_input)[offset_num:limit_num]

        serializers = ArticleSerializer(articles, many=True)

        articleJson = {'Articles': serializers.data}
        databaseMessageJson = {'Database Message':f"Database select query was successfully retrieved from the {Article.__name__} table." }

        responseJson = [articleJson, databaseMessageJson]
        return Response(responseJson)


        

            

