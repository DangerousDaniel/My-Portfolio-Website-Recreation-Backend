"""
    Project Name: My Portfolio Website Recreation
    Authors: Daniel Cox
    Created Date: April 21, 2023
    Last Updated: May 25, 2023
    Description: This is the class serialize all your data to JSON from a python object.
    Notes:
    Resources: 
 """

from rest_framework import serializers

from .models import Category

from .models import Paragraph
from .models import Paragraph_List

from .models import Image
from .models import Image_List

from .models import Video
from .models import Video_List

from .models import Resource
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

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image_id', 'name', 'description', 'link']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['video_id', 'name', 'link']

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['resource_id', 'name', 'description', 'link', 'image_link']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['article_id', 'name', 'author', 'summary', 'image_preview', 'category_id', 'max_order', 'date_created', 'date_last_update',]

class ParagraphListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph_List
        fields = ['paragraph_list_id ', 'paragraph_id', 'order', 'article_id']

class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image_List
        fields = ['image_list_id ', 'image_id', 'order', 'article_id']

class VideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video_List
        fields = ['video_list_id ', 'video_id', 'order', 'article_id']

class ResourceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource_List
        fields = ['resource_list_id', 'resource_id', 'article_id']