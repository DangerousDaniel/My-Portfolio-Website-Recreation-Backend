"""
    Project Name: My Portfolio Website Recreation
    Authors: Daniel Cox
    Created Date: April 26, 2023
    Last Updated: May 8, 2023
    Description: This is the class for article views.
    Notes:
    Resources: 
 """

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

        articles_json = []
        for article in articles:
            page_list = Page_List.objects.filter(article_id=article.article_id)
            resource_list = Resource_List.objects.filter(article_id=article.article_id)

            pages = [] 
            for p in page_list:
                pages.append(p.page_id)

            resources = []
            for r in resource_list:
                resources.append(r.resource_id)

            articleSerializer = ArticleSerializer(article)   
            pageSerializer = PageSerializer(pages, many=True)
            resourceSerializer = ResourceSerializer(resources, many=True)

            article = {'articleData': articleSerializer.data,
                       'pages': pageSerializer.data,
                       'resources': resourceSerializer.data}
            
            articles_json.append(article)


        json_data = {'articles': articles_json}
        
        database_error_json = {'error': False}
        database_message_json = {'message': f"Database select queries was successfully retrieved from the {Article.__name__} and the relationship tables."}
        database_list_json = [database_error_json, database_message_json]
        database_json = {'database': database_list_json}
        
        response_json = [json_data, database_json]
        return Response(response_json)
    
@api_view(['GET'])
def article_all_quick_view(request, offset_num=0, limit_num=30, format=None):
    if request.method == 'GET':
        articles = Article.objects.all().order_by('date_last_update').reverse()[offset_num:limit_num]

        serializer = ArticleSerializer(articles, many=True)

        article_json = {'articles': serializer.data}

        database_error_json = {'error': False}
        database_message_json = {'message': f"Database select queries was successfully retrieved from the {Article.__name__} table."}
        database_list_json = [database_error_json, database_message_json]
        database_json = {'database': database_list_json}
        
        response_json = [article_json, database_json]
        return Response(response_json)

@api_view(['GET'])
def article_all_quick_view_category(request, id, offset_num=0, limit_num=30, format=None):
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
        articles = Article.objects.filter(category_id=id).order_by('date_last_update').reverse()[offset_num:limit_num]

        serializer = ArticleSerializer(articles, many=True)

        article_json = {'articles': serializer.data}

        database_error_json = {'error': False}
        database_message_json = {'message': f"Database select queries was successfully retrieved from the {Article.__name__} table."}
        database_list_json = [database_error_json, database_message_json]
        database_json = {'database': database_list_json}
        
        response_json = [article_json, database_json]
        return Response(response_json)

@api_view(['GET'])
def article_detail(request, id, format=None):
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        database_error_json = {'error': True}
        database_message_json = {'message': f"No data found for this id in the {Article.__name__} table."}
        database_list_json = [database_error_json, database_message_json]
        database_json = {'database': database_list_json}
        
        response_json = [database_json]
        return Response(response_json, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        page_list = Page_List.objects.filter(article_id=id)
        resource_list = Resource_List.objects.filter(article_id=id)

        articleSerializer = ArticleSerializer(article)

        pages = []
        for page in page_list:
            pages.append(page.page_id)

        pageSerializer = PageSerializer(pages, many=True)
        
        resources = []
        for resource in resource_list:
            resources.append(resource.resource_id)
        
        resourceSerializer = ResourceSerializer(resources, many=True)
    
        page_context_json = {'pages': pageSerializer.data, 'resources': resourceSerializer.data}

        article_data_json = {f'article Data': articleSerializer.data, 'page Context': page_context_json}

        article_json = {'article': article_data_json}
        database_error_json = {'error': False}
        database_message_json = {'message': f"Database select queries was successfully retrieved from the {Article.__name__} and the relationship tables."}
        database_list_json = [database_error_json, database_message_json]
        database_json = {'database': database_list_json}
        
        response_json = [article_json, database_json]
        return Response(response_json)

@api_view(['DELETE'])
def article_delete_relationship_data(request, id, format=None):
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        database_error_json = {'error': True}
        database_message_json = {'message': f"No data found for this id in the {Article.__name__} table."}
        database_list_json = [database_error_json, database_message_json]
        database_json = {'database': database_list_json}
        
        response_json = [database_json]
        return Response(response_json, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        page_list = Page_List.objects.filter(article_id=id)
        resource_list = Resource_List.objects.filter(article_id=id)

        page_list.delete()
        resource_list.delete()
        article.delete()
        
        database_error_json = {'error': False}
        database_message_json = {'message': f"Data has successfully delete for this id in the {Article.__name__} and the relationship tables."}
        database_list_json = [database_error_json, database_message_json]
        database_json = {'database': database_list_json}
        
        response_json = [database_json]
        return Response(response_json, status=status.HTTP_204_NO_CONTENT)

            

