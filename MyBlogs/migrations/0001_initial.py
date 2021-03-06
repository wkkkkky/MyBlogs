# Generated by Django 3.0.3 on 2020-11-07 11:13

from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=30, unique=True, verbose_name='类别')),
            ],
            options={
                'verbose_name_plural': '类别',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30, unique=True, verbose_name='标签')),
            ],
            options={
                'verbose_name_plural': '标签',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='标题')),
                ('author', models.CharField(max_length=20, verbose_name='博客作者')),
                ('summary', models.TextField(max_length=100, verbose_name='博客摘要')),
                ('context', mdeditor.fields.MDTextField(blank=True, null=True, verbose_name='博客内容')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('watch_number', models.IntegerField(default=0, verbose_name='观看数')),
                ('is_valid', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyBlogs.Category', verbose_name='博客类别')),
                ('tag', models.ManyToManyField(to='MyBlogs.Tag', verbose_name='博客标签')),
            ],
            options={
                'verbose_name_plural': '文章',
                'ordering': ['-create_date'],
            },
        ),
    ]
