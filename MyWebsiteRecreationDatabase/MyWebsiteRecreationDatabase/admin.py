from django.contrib import admin
from .models import Category
from .models import Page_Context
from .models import Page
from .models import Page_List
from .models import Resource
from .models import Resource_List
from .models import Article

admin.site.register(Category)
admin.site.register(Page_Context)
admin.site.register(Page)
admin.site.register(Page_List)
admin.site.register(Resource)
admin.site.register(Resource_List)
admin.site.register(Article)