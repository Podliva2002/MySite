from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")

    class Meta:
        verbose_name_plural = 'Категории'
        ordering = ["pk"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    category = models.ManyToManyField(
        to=Category,
        related_name="products",
        verbose_name="Категории"
    )

    author = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        verbose_name="Автор"
    )

    class Meta:
        verbose_name_plural = 'Статьи'
        ordering = ["pk"]

    class Сomplexity(models.TextChoices):
        EASY = 'easy', 'Легкий',
        MEDIUM = 'medium', 'Средний',
        HARD = 'hard', 'Сложный',

    complexity = models.CharField(
        max_length=10,
        choices=Сomplexity.choices,
        default=Сomplexity.EASY,
        verbose_name="Сложность"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
