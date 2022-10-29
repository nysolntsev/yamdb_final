from datetime import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Genre(models.Model):
    name = models.CharField(
        'Name', max_length=100
    )
    slug = models.SlugField(
        'Slug', unique=True
    )
    description = models.TextField(
        'Description', blank=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        'Name', max_length=200
    )
    slug = models.SlugField(
        'Slug', unique=True
    )
    description = models.TextField(
        'Description', blank=True, null=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        'Name', max_length=300
    )
    year = models.PositiveIntegerField(verbose_name='Год выпуска',
                                       validators=[
                                           MinValueValidator(1200),
                                           MaxValueValidator(
                                               datetime.now().year)
                                       ])
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True, null=True,
        verbose_name='Категория',
        help_text='Выберите категорию'
    )
    rating = models.IntegerField(
        blank=True, null=True,
    )
    description = models.TextField(
        'Description', blank=True, null=True,
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        related_name='titles',
        verbose_name="Жанр"
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
