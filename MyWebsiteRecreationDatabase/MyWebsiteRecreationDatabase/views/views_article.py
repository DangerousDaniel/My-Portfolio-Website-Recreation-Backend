from ..models import Article, Page
from ..models import Page_List
from ..models import Resource_List

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
        

        

            

