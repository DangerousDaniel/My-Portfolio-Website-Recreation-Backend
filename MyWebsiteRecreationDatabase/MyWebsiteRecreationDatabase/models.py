"""
    Project Name: My Portfolio Website Recreation
    Authors: Daniel Cox
    Created Date: April 8, 2023
    Last Updated: May 24, 2023
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

    def __str__(self) -> str:
        return f"{self.paragraph}"
    
class Page_List(models.Model):
    page_list_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255) 
   
    def __str__(self):
        return  f"{self.name}"

class Page_Bridge(models.Model):
    page_bridge_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    page_id = models.ForeignKey(Page, on_delete=models.PROTECT)
    order = models.IntegerField()
    page_list_id = models.ForeignKey(Page_List, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.page_id} | {self.page_id} | {self.order} | {self.page_list_id}"
 
class Image(models.Model):
    image_id =  models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name} | {self.description} | {self.link}"

class Image_List(models.Model):
    image_list_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
 
    def __str__(self):
        return  f"{self.name}"

class Image_Bridge(models.Model):
    image_bridge_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    image_id = models.ForeignKey(Image, on_delete=models.PROTECT)
    order = models.IntegerField()
    image_list_id = models.ForeignKey(Image_List, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.image_id} | {self.image_id} | {self.order} | {self.image_list_id}"

class Video(models.Model):
    video_id =  models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name} | {self.link}"

class Video_List(models.Model):
    video_list_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return  f"{self.name}"

class Video_Bridge(models.Model):
    video_bridge_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    video_id = models.ForeignKey(Video, on_delete=models.PROTECT)
    order = models.IntegerField()
    video_list_id = models.ForeignKey(Video_List, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.video_id} | {self.video_id} | {self.order} | {self.video_bridge_id}"

class Resource(models.Model):
    resource_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=255)
    image_link =  models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return f"{self.name} | {self.description} | {self.link}"

class Resource_List(models.Model):
    resource_list_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)

    def __str__(self):
        return  f"{self.name}"

class Resource_Bridge(models.Model):
    resource_bridge_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    resource_id = models.ForeignKey(Resource, on_delete=models.PROTECT)
    resource_list_id = models.ForeignKey(Resource_List, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return f"{self.resource_id} | {self.resource_id} | {self.resource_list_id}"

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
    page_list_id = models.ForeignKey(Page_List, on_delete=models.PROTECT)
    image_list_id = models.ForeignKey(Image_List, on_delete=models.PROTECT)
    video_lits_id = models.ForeignKey(Video_List, on_delete=models.PROTECT, blank=True, null=True)
    resource_list_id = models.ForeignKey(Resource_List, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.name} | {self.author} | {self.image_preview} | {self.category_id} | {self.date_created} | {self.date_last_update} | {self.page_list_id} | {self.image_list_id} | {self.video_lits_id} | {self.resource_list_id}"

class About(models.Model):
    about_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_link = models.CharField(max_length=255)

    def __str__(self):
        return  f"{self.name} | {self.description} | {self.image_link}"

class Resume(models.Model):
    resume_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    resource_list_id = models.ForeignKey(Resource_List, on_delete=models.PROTECT)

    def __str__(self):
        return  f"{self.name} | {self.resource_list_id}"
    
class Footer_Information(models.Model):
    footer_information_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    description = models.TextField()
    resource_list_id = models.ForeignKey(Resource_List, on_delete=models.PROTECT)

    def __str__(self):
        return  f"{self.name} | {self.description} | {self.resource_list_id}"