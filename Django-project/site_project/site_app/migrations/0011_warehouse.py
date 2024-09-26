# Generated by Django 5.1 on 2024-09-05 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0010_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Наименование')),
                ('article_number', models.CharField(max_length=100, verbose_name='Артикул')),
                ('manufacturer', models.CharField(max_length=200, null=True, verbose_name='Производитель')),
                ('serial_number', models.CharField(max_length=100, unique=True, verbose_name='Серийный номер')),
                ('warehouse', models.CharField(choices=[('OTS_GPT', 'ОТС.ГПТ'), ('OTS', 'ОТС.')], default='OTS_GPT', max_length=50, verbose_name='Склад')),
                ('email', models.EmailField(max_length=100, verbose_name='Почта')),
                ('return_date', models.DateField(verbose_name='Дата возврата')),
                ('location', models.CharField(default='Не указано', max_length=1000, verbose_name='Местоположение')),
                ('bundle', models.CharField(choices=[('None', 'Неизвестно'), ('Full', 'Полный комплект'), ('Partial', 'Частичный комплект')], default='None', max_length=40, verbose_name='Комплектность')),
                ('status', models.CharField(choices=[('Issued', 'Выдан'), ('Returned', 'Возвращен'), ('Expired', 'Просрочен')], default='Issued', max_length=50, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'взятое оборудование',
                'verbose_name_plural': 'Склад',
            },
        ),
    ]
