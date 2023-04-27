"""
    Project Name: My Portfolio Website Recreation
    Authors: Daniel Cox
    Created Date: April 8, 2023
    Last Updated: April 21, 2023
    Description: This where you create the table for the database.
    Notes:
    Resources: 
 """

from django.db import models

class Category(models.Model):
    category_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"

class Page(models.Model):
    page_id =  models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    paragraph = models.TextField()
    image_file = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return f"{self.paragraph} | {self.image_file}"

class Resource(models.Model):
    resource_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name} | {self.link}"

class Article(models.Model):
    article_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.TextField()
    image_preview = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    date_created = models.DateField()
    date_last_update = models.DateField(auto_created=True)

    def __str__(self) -> str:
        return f"{self.name} | {self.author} | {self.image_preview} | {self.category_id} | {self.date_created} | {self.date_last_update}"

class Page_List(models.Model):
    page_list_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    page_id = models.ForeignKey(Page, on_delete=models.PROTECT)
    article_id = models.ForeignKey(Article, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.page_id} | {self.article_id}"

class Resource_List(models.Model):
    resource_list_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    resource_id = models.ForeignKey(Resource, on_delete=models.PROTECT)
    article_id = models.ForeignKey(Article, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return f"{self.resource_id} | {self.article_id}"




    