# Generated by Django 4.2 on 2023-05-02 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_type_alter_blog_body_alter_blog_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
