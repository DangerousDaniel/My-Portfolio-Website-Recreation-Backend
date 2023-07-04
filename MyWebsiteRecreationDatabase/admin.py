"""
    Project Name: My Portfolio Website Recreation
    Authors: Daniel Cox
    Created Date: April 21, 2023
    Last Updated: July 3, 2023
    Description: This is the class for registering your all table to the Django Admin. 
    Notes:
    Resources: 
 """

from django.contrib import admin

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

#region Admin Registration
admin.site.register(Category)
admin.site.register(Paragraph)
admin.site.register(Paragraph_List)
admin.site.register(Image)
admin.site.register(Image_List)
admin.site.register(Video)
admin.site.register(Video_List)
admin.site.register(Resource)
admin.site.register(Resource_List)
#endregion

#region Registration of Custom Forum
class ParagraphListInLine(admin.TabularInline):
    model = Paragraph_List

class ImageListInLine(admin.TabularInline):
    model = Image_List

class VideoListInLine(admin.TabularInline):
    model = Video_List

class ResourceListInLine(admin.TabularInline):
    model = Resource_List

class ArticleAdminForm(admin.ModelAdmin):
    inlines = [ParagraphListInLine, ImageListInLine, VideoListInLine, ResourceListInLine]

admin.site.register(Article, ArticleAdminForm)
#endregion