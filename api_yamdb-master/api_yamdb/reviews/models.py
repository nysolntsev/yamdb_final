from django.db import models

from titles.models import Title
from users.models import User


choice_score = list((i, i) for i in range(1, 11))


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
    )
    text = models.TextField(
        'Текст отзыва',
        help_text='Напишите текст отзыва',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='r_author',
        verbose_name='Автор отзыва',
    )
    score = models.PositiveSmallIntegerField(
        'Оценка',
        help_text='Выберите оценку от 1 до 10',
        choices=choice_score,
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='dont_review_twice'
            )
        ]
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.text[:10]}, {self.author}'


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв',
    )
    text = models.TextField(
        'Текст комментария',
        help_text='Ввдите текст комментария',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='c_author',
        verbose_name='Автор комментария',
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.text[:15]}, {self.author}'
