# Generated by Django 2.2.5 on 2019-09-16 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='blog_id',
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='author_id',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
