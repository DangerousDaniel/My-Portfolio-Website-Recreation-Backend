"""
    Project Name: My Portfolio Website Recreation
    Authors: Daniel Cox
    Created Date: April 26, 2023
    Last Updated: May 3, 2023
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

            article = {'ArticleData': articleSerializer.data,
                       'PageData': pageSerializer.data,
                       'ResourceData': resourceSerializer.data}
            
            articles_json.append(article)


        jsonData = {'Articles': articles_json}
        database_message_json = {'Database Message':  f"Database select queries was successfully retrieved from the {Article.__name__} and the relationship tables." }

        response = [jsonData, database_message_json]
        return Response(response)
    
@api_view(['GET'])
def article_all_category(request, id, format=None):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        database_message_json= {'Database Message': f"No data found for this id in the {Category.__name__} table."}
        response_json = database_message_json
        return Response(response_json, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        articles = Article.objects.filter(category_id=id)

        articles_json = []
        for article in articles:
            page_list = Page_List.objects.filter(article_id=article.article_id)
            resource_list = Resource_List.objects.filter(article_id=article.article_id)

            pages = [] 
            for page in page_list:
                pages.append(page.page_id)

            resources = []
            for resource in resource_list:
                resources.append(resource.resource_id)

            articleSerializer = ArticleSerializer(article)   
            pageSerializer = PageSerializer(pages, many=True)
            resourceSerializer = ResourceSerializer(resources, many=True)

            article = {'ArticleData': articleSerializer.data,
                       'PageData': pageSerializer.data,
                       'ResourceData': resourceSerializer.data}
            
            articles_json.append(article)


        jsonData = {'Articles': articles_json}
        database_message_json = {'Database Message':  f"Database select queries was successfully retrieved from the {Article.__name__} and the relationship tables." }

        response = [jsonData, database_message_json]
        return Response(response)

    
@api_view(['GET'])
def article_all_quick_view(request, offset_num=0, limit_num=10, format=None):
    if request.method == 'GET':
        articles = Article.objects.all().order_by('date_last_update').reverse()[offset_num:limit_num]

        serializer = ArticleSerializer(articles, many=True)

        article_json = {'Articles': serializer.data}
        database_message_json = {'Database Message':f"Database select query was successfully retrieved from the {Article.__name__} table." }

        response_json = [article_json, database_message_json]
        return Response(response_json)


@api_view(['GET'])
def article_all_quick_view_category(request, id, offset_num=0, limit_num=10, format=None):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        database_message_json= {'Database Message': f"No data found for this id in the {Category.__name__} table."}
        response_json = database_message_json
        return Response(response_json, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        articles = Article.objects.filter(category_id=id).order_by('date_last_update').reverse()[offset_num:limit_num]

        serializer = ArticleSerializer(articles, many=True)

        article_json = {'Articles': serializer.data}
        database_message_json = {'Database Message':f"Database select query was successfully retrieved from the {Article.__name__} table." }

        response_json = [article_json, database_message_json]
        return Response(response_json)

@api_view(['GET'])
def article_detail(request, id, format=None):
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        database_message_json= {'Database Message': f"No data found for this id in the {Article.__name__} table."}
        response_json = database_message_json
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
    
        page_context_json = {'Pages': pageSerializer.data, 'Resources': resourceSerializer.data}

        article_data_json = {f'Article Data': articleSerializer.data, 'Page Context': page_context_json}

        article_json = {f'Article {id}': article_data_json}
        database_message_json = {'Database Message':  f"Database select queries was successfully retrieved from the {Article.__name__} and the relationship tables." }

        response_json = [article_json, database_message_json]
        return Response(response_json)


@api_view(['DELETE'])
def article_delete_relationship_data(request, id, format=None):
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        database_message_json= {'Database Message': f"No data found for this id in the {Article.__name__} table."}
        response_json = database_message_json
        return Response(response_json, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        page_list = Page_List.objects.filter(article_id=id)
        resource_list = Resource_List.objects.filter(article_id=id)

        page_list.delete()
        resource_list.delete()
        article.delete()
        
        database_message_json = {'Database Message':  f"Data has successfully delete for this id in the {Article.__name__} and the relationship tables." }

        response_json = [database_message_json]
        return Response(response_json)

            

