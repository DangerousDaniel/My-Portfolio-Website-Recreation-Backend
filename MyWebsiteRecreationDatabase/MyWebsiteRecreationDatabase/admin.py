"""
    Project Name: My Portfolio Website Recreation
    Authors: Daniel Cox
    Created Date: April 21, 2023
    Last Updated: April 26, 2023
    Description: This is the class for registering your all table to the Django Admin. 
    Notes:
    Resources: 
 """

from django.contrib import admin
from .models import Category
from .models import Page
from .models import Page_List
from .models import Resource
from .models import Resource_List
from .models import Article

#region Admin Registration
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Page_List)
admin.site.register(Resource)
admin.site.register(Resource_List)
#endregion

#region Registration of Custom Forum
class PageListInLine(admin.TabularInline):
    model = Page_List

class ResourceListInLine(admin.TabularInline):
    model = Resource_List

class ArticleAdminForm(admin.ModelAdmin):
    inlines = [PageListInLine, ResourceListInLine]

admin.site.register(Article, ArticleAdminForm)
#endregion