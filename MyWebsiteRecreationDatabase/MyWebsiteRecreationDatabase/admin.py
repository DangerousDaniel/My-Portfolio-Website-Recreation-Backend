"""
    Project Name: My Portfolio Website Recreation
    Authors: Daniel Cox
    Created Date: April 21, 2023
    Last Updated: May 23, 2023
    Description: This is the class for registering your all table to the Django Admin. 
    Notes:
    Resources: 
 """

from django.contrib import admin

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

admin.site.register(Category)

admin.site.register(Page)
admin.site.register(Page_Bridge)
admin.site.register(Page_List)

admin.site.register(Image)
admin.site.register(Image_Bridge)
admin.site.register(Image_List)

admin.site.register(Video)
admin.site.register(Video_Bridge)
admin.site.register(Video_List)

admin.site.register(Resource)
admin.site.register(Resource_Bridge)
admin.site.register(Resource_List)

admin.site.register(Article)

admin.site.register(About)
admin.site.register(Resume)
admin.site.register(Footer_Information)
