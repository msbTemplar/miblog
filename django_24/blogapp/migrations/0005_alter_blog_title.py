# Generated by Django 5.0.4 on 2024-05-01 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_blog_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
