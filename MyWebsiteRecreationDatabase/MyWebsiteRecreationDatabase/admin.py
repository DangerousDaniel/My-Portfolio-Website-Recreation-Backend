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
from .models import Article


admin.site.register(Category)
admin.site.register(Article)
