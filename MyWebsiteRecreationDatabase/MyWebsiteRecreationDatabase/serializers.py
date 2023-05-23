"""
    Project Name: My Portfolio Website Recreation
    Authors: Daniel Cox
    Created Date: April 21, 2023
    Last Updated: May 23, 2023
    Description: This is the class serialize all your data to JSON from a python object.
    Notes:
    Resources: 
 """

from rest_framework import serializers

from .models import Category

from .models import Page
from .models import Page_Bridge
from .models import Page_List

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

from .models import About
from .models import Resume
from .models import Footer_Information

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'name']

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['page_id', 'paragraph']

class PageBridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page_Bridge
        fields = ['page_bridge_id', 'page_id', 'order']

class PageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page_List
        fields = ['page_list_id ', 'name', 'page_bridge_id']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image_id', 'name', 'link']

class ImageBridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image_Bridge
        fields = ['image_bridge_id', 'image_id', 'order']

class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image_List
        fields = ['image_list_id ', 'name', 'image_bridge_id']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['video_id', 'name', 'link']

class VideoBridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video_Bridge
        fields = ['video_bridge_id', 'video_id', 'order']

class VideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video_List
        fields = ['video_list_id ', 'name', 'video_bridge_id']

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['resource_id', 'name', 'description', 'link', 'image_link']

class ResourceBridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource_Bridge
        fields = ['resource_bridge_id', 'resource_id']

class ResourceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource_List
        fields = ['resource_list_id', 'name', 'resource_bridge_id']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['article_id', 'name', 'author', 'summary', 'image_preview', 'category_id', 'max_order', 'date_created', 'date_last_update', 'page_list_id', 'image_list_id', 'video_lits_id', 'resource_list_id']

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['about_id', 'name', 'description', 'image_link']

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['resume_id', 'name', 'resource_list_id']

class FooterInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer_Information
        fields = ['footer_information_id', 'name', 'description', 'resource_list_id']