"""
    Project Name: My Portfolio Website Recreation
    Authors: Daniel Cox
    Created Date: April 21, 2023
    Last Updated: April 26, 2023
    Description: This class is where you create all the urls for your REST API.
    Notes:
    Resources: 
 """

"""MyWebsiteRecreationDatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from MyWebsiteRecreationDatabase.views import views_category
from MyWebsiteRecreationDatabase.views import views_article

urlpatterns = [
    path('admin/', admin.site.urls),

    path('category/all', views_category.category_all),
    path('article/all', views_article.article_all),
    path('article/all/quick-view/<int:category_id_input>', views_article.article_all_quick_view),
    path('article/all/quick-view/<int:category_id_input>/<int:offset_num>/<int:limit_num>', views_article.article_all_quick_view),
    path('article/detail/<int:id>', views_article.article_detail),
    path('article/delete-relationship-data/<int:id>', views_article.article_delete_relationship_data),

]

urlpatterns = format_suffix_patterns(urlpatterns)