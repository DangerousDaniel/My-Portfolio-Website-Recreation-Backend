from django.db import models

class Category(models.Model):
    category_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.category_id} | {self.name}"

class Page(models.Model):
    page_id =  models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    paragraph = models.TextField()
    image_file = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return f"{self.page_id} | {self.paragraph} | {self.image_file}"

class Page_Context(models.Model):
    page_context_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')

    def __str__(self):
        return f"{__class__.__name__} {self.page_context_id}"
    
class Page_list(models.Model):
    page_list_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    page_id = models.ManyToManyField(Page)
    page_context_id = models.ForeignKey(Page_Context, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.page_context_id} | {self.page_id} | {self.page_context_id}"

class Resource(models.Model):
    resource_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.resource_id} | {self.link}"

class Resource_List(models.Model):
    resource_list_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    resource_id = models.ManyToManyField(Resource)
    page_context_id = models.ForeignKey(Page_Context, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return f"{self.page_context_id} | {self.resource_id} | {self.page_context_id}"

class Article(models.Model):
    article_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.TextField()
    image_preview = models.CharField(max_length=255)
    category_id = models.OneToOneField(Category, on_delete=models.PROTECT)
    Page_Context_id = models.OneToOneField(Page_Context, on_delete=models.PROTECT)
    date_created = models.DateField()
    date_last_update = models.DateField(auto_created=True)

    def __str__(self) -> str:
        return f"{self.article_id} | {self.name} | {self.author} | {self.image_preview} | {self.category_id} | {self.Page_Context_id} | {self.date_created} | {self.date_last_update}"


    