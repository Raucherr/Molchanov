# Generated by Django 4.0.3 on 2022-03-27 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_tag_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
