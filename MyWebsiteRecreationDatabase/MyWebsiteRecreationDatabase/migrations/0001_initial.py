# Generated by Django 3.2.17 on 2023-04-26 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('date_last_update', models.DateField(auto_created=True)),
                ('article_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('image_preview', models.CharField(max_length=255)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('page_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField()),
                ('image_file', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('resource_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Resource_List',
            fields=[
                ('resource_list_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyWebsiteRecreationDatabase.article')),
                ('resource_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyWebsiteRecreationDatabase.resource')),
            ],
        ),
        migrations.CreateModel(
            name='Page_List',
            fields=[
                ('page_list_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyWebsiteRecreationDatabase.article')),
                ('page_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyWebsiteRecreationDatabase.page')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyWebsiteRecreationDatabase.category'),
        ),
    ]
