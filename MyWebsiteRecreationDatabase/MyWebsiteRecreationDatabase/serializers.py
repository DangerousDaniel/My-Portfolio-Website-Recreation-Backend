"""
    Project Name: My Portfolio Website Recreation
    Authors: Daniel Cox
    Created Date: April 21, 2023
    Last Updated: May 24, 2023
    Description: This is the class serialize all your data to JSON from a python object.
    Notes:
    Resources: 
 """

from rest_framework import serializers

from .models import Category

from .models import Paragraph
from .models import Paragraph_Bridge
from .models import Paragraph_List

from .models import Image
from .models import Image_Bridge
from .models import Image_List

from .models import Video
from .models import Video_Bridge
from .models import Video_List

from .models import Resource
from .models import Resource_Bridge
from .models import Resource_List

from .models import Article

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'name']

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['paragraph_id', 'name', 'description']

class ParagraphBridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph_Bridge
        fields = ['paragraph_bridge_id', 'page_id', 'order', 'paragraph_list_id']

class ParagraphListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph_List
        fields = ['paragraph_list_id ', 'name']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image_id', 'name', 'description', 'link']

class ImageBridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image_Bridge
        fields = ['image_bridge_id', 'image_id', 'order', 'image_list_id']

class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image_List
        fields = ['image_list_id ', 'name']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['video_id', 'name', 'link']

class VideoBridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video_Bridge
        fields = ['video_bridge_id', 'video_id', 'order', 'video_list_id']

class VideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video_List
        fields = ['video_list_id ', 'name']

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['resource_id', 'name', 'description', 'link', 'image_link']

class ResourceBridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource_Bridge
        fields = ['resource_bridge_id', 'resource_id', 'resource_list_id']

class ResourceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource_List
        fields = ['resource_list_id', 'name']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['article_id', 'name', 'author', 'summary', 'image_preview', 'category_id', 'max_order', 'date_created', 'date_last_update', 'paragraph_list_id', 'image_list_id', 'video_lits_id', 'resource_list_id']