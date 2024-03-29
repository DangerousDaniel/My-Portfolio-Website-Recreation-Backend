# Generated by Django 3.2.18 on 2023-05-25 22:05

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
                ('max_order', models.IntegerField()),
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
            name='Image',
            fields=[
                ('image_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('paragraph_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('resource_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=255)),
                ('image_link', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('video_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Video_List',
            fields=[
                ('video_list_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyWebsiteRecreationDatabase.article')),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyWebsiteRecreationDatabase.video')),
            ],
        ),
        migrations.CreateModel(
            name='Resource_List',
            fields=[
                ('resource_bridge_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyWebsiteRecreationDatabase.article')),
                ('resource_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyWebsiteRecreationDatabase.resource')),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph_List',
            fields=[
                ('paragraph_list_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyWebsiteRecreationDatabase.article')),
                ('paragraph_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyWebsiteRecreationDatabase.paragraph')),
            ],
        ),
        migrations.CreateModel(
            name='Image_List',
            fields=[
                ('image_list_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyWebsiteRecreationDatabase.article')),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyWebsiteRecreationDatabase.image')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MyWebsiteRecreationDatabase.category'),
        ),
    ]
