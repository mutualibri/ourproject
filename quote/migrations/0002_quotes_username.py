# Generated by Django 4.2.5 on 2023-12-11 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='username',
            field=models.TextField(null=True),
        ),
    ]
