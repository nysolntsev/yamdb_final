from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class UserManager(UserManager):

    def create_user(self, username, email, password, **extra_fields):
        return super().create_user(
            username=username, email=email, password=password, **extra_fields)

    def create_superuser(self, username,
                         email, password,
                         role='admin', **extra_fields):
        return super().create_superuser(
            username=username,
            email=email,
            password=password,
            role=role,
            **extra_fields
        )


class User(AbstractUser):
    CHOICES = (
        ('user', 'user'),
        ('admin', 'admin'),
        ('moderator', 'moderator'),
    )
    role = models.CharField(max_length=40, choices=CHOICES, default='user')
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    username = models.CharField(max_length=150, unique=True)
    objects = UserManager()

    REQUIRED_FIELDS = ('email', 'password')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'

    def __str__(self):
        return (self.username, self.role)

    @property
    def is_admin(self):
        return self.role == self.CHOICES[1][0]

    @property
    def is_moderator(self):
        return self.role == self.CHOICES[2][0]
