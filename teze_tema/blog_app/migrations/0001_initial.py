# Generated by Django 2.2.5 on 2019-09-16 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('short_content', models.CharField(max_length=255)),
                ('full_content', models.TextField()),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.Blogs')),
            ],
        ),
    ]
