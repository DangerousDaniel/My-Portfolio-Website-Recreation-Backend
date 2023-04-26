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

        serializer = ArticleSerializer(articles, many=True)        

        article_json = {'Articles': serializer.data}
        database_message_json = {'Database Message':f"Database select query was successfully retrieved from the {Article.__name__} table." }

        response_json = [article_json, database_message_json]
        return Response(response_json)


@api_view(['GET'])
def article_all_quick_view(request, category_id_input, offset_num=0, limit_num=10, format=None):
    try:
        category = Category.objects.get(pk=category_id_input)
    except Category.DoesNotExist:
        database_message_json= {'Database Message': f"No data found for this id in the {Category.__name__} table."}
        response = database_message_json
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        articles = Article.objects.filter(category_id=category_id_input)[offset_num:limit_num]

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
        response = database_message_json
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    
    try: 
        page_list = Page_List.objects.filter(article_id=id)
    except Page_List.DoesNotExist:
        database_message_json= {'Database Message': f"No data found for this id in the {Page_List.__name__} table."}
        response = database_message_json
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    try: 
        resource_list = Resource_List.objects.filter(article_id=id)
    except Resource_List.DoesNotExist:
        database_message_json= {'Database Message': f"No data found for this id in the {Resource_List.__name__} table."}
        response = database_message_json
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
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




        
        

            

