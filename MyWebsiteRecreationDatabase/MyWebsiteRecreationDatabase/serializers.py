from rest_framework import serializers
from .models import Category
from .models import Page
from .models import Page_List
from .models import Resource
from .models import Resource_List
from .models import Article

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'name']

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['page_id', 'paragraph', 'image_file']

class PageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page_List
        fields = ['page_list_id', 'page_id', 'article_id']

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['resource_id', 'name', 'link']

class ResourceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource_List
        fields = ['resource_list_id', 'resource_id', 'article_id']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['article_id', 'name', 'author', 'summary', 'image_preview', 'category_id', 'date_created', 'date_last_update']
