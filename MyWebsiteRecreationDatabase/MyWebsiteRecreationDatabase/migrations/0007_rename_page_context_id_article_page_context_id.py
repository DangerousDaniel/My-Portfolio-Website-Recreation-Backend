# Generated by Django 3.2.18 on 2023-04-22 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyWebsiteRecreationDatabase', '0006_resource_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Page_Context_id',
            new_name='Page_context_id',
        ),
    ]
