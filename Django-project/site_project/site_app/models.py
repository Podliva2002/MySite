from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")

    class Meta:
        verbose_name_plural = 'Категория'
        ordering = ["pk"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    category = models.ManyToManyField(
        to=Category,
        related_name="products",
        verbose_name="Категории"
    )

    class Meta:
        verbose_name_plural = 'Товары'
        ordering = ["pk"]

    class Condition(models.TextChoices):
        NEW = 'new', 'Новый',
        USED = 'used', 'Б/У'

    condition = models.CharField(
        max_length=10,
        choices=Condition.choices,
        default=Condition.NEW,
        verbose_name="Состояние"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
