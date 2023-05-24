"""
    Project Name: My Portfolio Website Recreation
    Authors: Daniel Cox
    Created Date: April 26, 2023
    Last Updated: May 23, 2023
    Description: This is the class for article views.
    Notes:
    Resources: 
 """

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Page
from ..models import Page_Bridge
from ..models import Page_List

from ..models import Image
from ..models import Image_Bridge
from ..models import Image_List

from ..models import Video
from ..models import Video_Bridge
from ..models import Video_List

from ..models import Resource
from ..models import Resource_Bridge
from ..models import Resource_List

from ..models import Article

from ..models import About
from ..models import Resume
from ..models import Footer_Information

from ..serializers import ArticleSerializer
from ..serializers import PageSerializer
from ..serializers import ImageSerializer
from ..serializers import VideoSerializer
from ..serializers import ResourceSerializer

@api_view(['GET'])
def article_all(request, format=None):
      if request.method == 'GET':
        articles = Article.objects.all()

        articles_json = []
        for article in articles:    
        
            page_bridge = Page_Bridge.objects.filter(page_list_id=article.page_list_id)
            image_bridge = Image_Bridge.objects.filter(image_list_id=article.image_list_id)
            video_bridge = Video_Bridge.objects.filter(video_list_id=article.video_lits_id)
            resource_bridge = Resource_Bridge.objects.filter(resource_list_id=article.resource_list_id)

            pages = []
            for pb in page_bridge:
                pages.append(pb.page_id)

            images = []
            for ib in image_bridge:
                images.append(ib.image_id)

            videos = []
            for vb in video_bridge:
                videos.append(vb.video_id)
            
            resources = []
            for rb in resource_bridge:
                resources.append(rb.resource_id)
            
            articleSerializer = ArticleSerializer(article)
            pageSerializer = PageSerializer(pages, many=True)
            imageSerializer = ImageSerializer(images, many=True)
            videoSerializer = VideoSerializer(videos, many=True)
            resourceSerializer = ResourceSerializer(resources, many=True)

            article_json = {'articleData': articleSerializer.data,
                            'pages': pageSerializer.data,
                            'images': imageSerializer.data,
                            'videos': videoSerializer.data,
                            'resources': resourceSerializer.data}
            
            articles_json.append(article_json)

            json_data = {'articles': articles_json}
        
        database_error_json = {'error': False}
        database_message_json = {'message': f"Database select queries was successfully retrieved from the {Article.__name__} and the relationship tables."}
        database_list_json = [database_error_json, database_message_json]
        database_json = {'database': database_list_json}
        
        response_json = [json_data, database_json]
        return Response(response_json)

    
@api_view(['GET'])
def article_all_quick_view(request, offset_num=0, limit_num=30, format=None):
   pass

@api_view(['GET'])
def article_all_quick_view_category(request, id, offset_num=0, limit_num=30, format=None):
   pass

@api_view(['GET'])
def article_detail(request, id, format=None):
    pass

@api_view(['DELETE'])
def article_delete_relationship_data(request, id, format=None):
    pass
            

