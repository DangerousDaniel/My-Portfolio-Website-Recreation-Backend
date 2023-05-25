"""
    Project Name: My Portfolio Website Recreation
    Authors: Daniel Cox
    Created Date: April 8, 2023
    Last Updated: May 25, 2023
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

class Paragraph(models.Model):
    paragraph_id =  models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255) 
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.name} | {self.description}"
 
class Image(models.Model):
    image_id =  models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name} | {self.description} | {self.link}"

class Video(models.Model):
    video_id =  models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name} | {self.link}"

class Resource(models.Model):
    resource_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=255)
    image_link =  models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return f"{self.name} | {self.description} | {self.link} | {self.image_link}"

class Article(models.Model):
    article_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.TextField()
    image_preview = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    max_order = models.IntegerField() 
    date_created = models.DateField()
    date_last_update = models.DateField(auto_created=True)

    def __str__(self) -> str:
        return f"{self.name} | {self.author} | {self.summary} | {self.image_preview} | {self.category_id} | {self.date_created} | {self.date_last_update}"
    
class Paragraph_List(models.Model):
    paragraph_list_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    paragraph_id = models.ForeignKey(Paragraph, on_delete=models.PROTECT)
    order = models.IntegerField()
    article_id = models.ForeignKey(Article, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.paragraph_id} | {self.order} | {self.article_id}"
    
class Image_List(models.Model):
    image_list_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    image_id = models.ForeignKey(Image, on_delete=models.PROTECT)
    order = models.IntegerField()
    article_id = models.ForeignKey(Article, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.image_id} | {self.image_id} | {self.order} | {self.article_id}"
    
class Video_List(models.Model):
    video_list_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    video_id = models.ForeignKey(Video, on_delete=models.PROTECT)
    order = models.IntegerField()
    article_id = models.ForeignKey(Article, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.video_id} | {self.video_id} | {self.order} | {self.article_id}"
    
class Resource_List(models.Model):
    resource_bridge_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    resource_id = models.ForeignKey(Resource, on_delete=models.PROTECT)
    article_id = models.ForeignKey(Article, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return f"{self.resource_id} | {self.resource_id} | {self.article_id}"