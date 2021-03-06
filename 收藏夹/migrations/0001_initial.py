# Generated by Django 2.2 on 2020-08-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urlclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('abstract', models.TextField(verbose_name='摘要')),
                ('url', models.URLField(verbose_name='网址')),
            ],
            options={
                'verbose_name': '收藏的网址',
                'verbose_name_plural': '收藏的网址',
            },
        ),
    ]
