# Generated by Django 3.2.18 on 2023-04-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWebsiteRecreationDatabase', '0003_article_page_page_list_resource_resource_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_last_update',
            field=models.DateTimeField(auto_created=True),
        ),
    ]