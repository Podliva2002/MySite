# Generated by Django 5.1 on 2024-08-14 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0007_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
