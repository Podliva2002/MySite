from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

UserModel = get_user_model()


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")

    class Meta:
        verbose_name_plural = 'Категории'
        ordering = ["pk"]

    def get_absolute_url(self):
        return reverse("site_app:category-detail", kwargs={"pk": self.pk})

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


def get_absolute_url():
    return reverse('site_app:index')


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=1000)

    class Meta:
        verbose_name = "Заявки из формы связи"
        ordering = ["pk"]

    def __str__(self):
        return f"Заявка от {self.name}-{self.email}"



