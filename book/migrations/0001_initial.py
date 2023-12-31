# Generated by Django 4.2.4 on 2023-10-29 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('author', models.TextField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('voters', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('currency', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('publisher', models.TextField(blank=True, null=True)),
                ('page_count', models.IntegerField(blank=True, null=True)),
                ('generes', models.TextField(blank=True, null=True)),
                ('ISBN', models.IntegerField(blank=True, null=True)),
                ('language', models.TextField(blank=True, null=True)),
                ('published_date', models.TextField(blank=True, null=True)),
                ('image', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
