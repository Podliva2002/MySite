# Generated by Django 5.1 on 2024-09-02 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0009_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Заявки из формы связи',
                'ordering': ['pk'],
            },
        ),
    ]
