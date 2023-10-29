# Generated by Django 4.2.4 on 2023-10-27 11:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20231024_1016'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='books',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.book'),
        ),
        migrations.AlterField(
            model_name='item',
            name='rating',
            field=models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0, message='Rating cannot be negative'), django.core.validators.MaxValueValidator(100, message='Maximum rating is 100')]),
        ),
        migrations.AlterField(
            model_name='item',
            name='review',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_added',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='dislikes_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='likes_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
