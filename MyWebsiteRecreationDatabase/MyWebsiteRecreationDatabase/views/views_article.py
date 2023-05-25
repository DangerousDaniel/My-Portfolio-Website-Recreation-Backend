"""
    Project Name: My Portfolio Website Recreation
    Authors: Daniel Cox
    Created Date: April 26, 2023
    Last Updated: May 25, 2023
    Description: This is the class for article views.
    Notes:
    Resources: 
 """

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Paragraph
from ..models import Paragraph_Bridge
from ..models import Paragraph_List

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
from ..serializers import ParagraphSerializer
from ..serializers import ImageSerializer
from ..serializers import VideoSerializer
from ..serializers import ResourceSerializer

@api_view(['GET'])
def article_all(request, format=None):
      if request.method == 'GET':
        articles = Article.objects.all()

        articles_json = []
        for article in articles:    
        
            paragraph_bridge = Paragraph_Bridge.objects.filter(paragraph_list_id=article.paragraph_list_id)
            image_bridge = Image_Bridge.objects.filter(image_list_id=article.image_list_id)
            video_bridge = Video_Bridge.objects.filter(video_list_id=article.video_lits_id)
            resource_bridge = Resource_Bridge.objects.filter(resource_list_id=article.resource_list_id)

            paragraph = []
            for pb in paragraph_bridge:
                paragraph.append(pb.paragraph_id)

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
            resourceSerializer = ResourceSerializer(resources, many=True)
            
            page_context_json_oder = []
            for i in range(article.max_order + 1):
                for pb in paragraph_bridge:
                    if i == pb.order:
                        paragraphSerializer = ParagraphSerializer(pb.paragraph_id)
                        paragraph = {'paragraph': paragraphSerializer.data}
                        page_context_json_oder.append(paragraph)

                for ib in image_bridge:
                    if i == ib.order:
                        imageSerializer = ImageSerializer(ib.image_id)
                        image = {'image': imageSerializer.data}
                        page_context_json_oder.append(image)

                for vb in video_bridge:
                    if i == vb.order:
                        videoSerializer = VideoSerializer(vb.video_id)
                        video = {'video': videoSerializer.data}
                        page_context_json_oder.append(video)

            resources_json = {'resources': resourceSerializer.data}
            page_context_json_oder.append(resources_json)

            article_json = {'articleData': articleSerializer.data, 'page_context': page_context_json_oder}
            
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
   pass

@api_view(['GET'])
def article_detail(request, id, format=None):
    pass
            

