from django.conf import settings
from rest_framework import exceptions, serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        fields = (
            'username',
            'email',
            'role',
            'bio',
            'first_name',
            'last_name',
        )
        model = User
        read_only_fields = ('role',)

    def validate_username(self, value):
        if value == settings.RESERVED_NAME:
            raise serializers.ValidationError(
                f'Нельзя использовать юзернейм {settings.RESERVED_NAME}')
        return value


class AdminSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        fields = (
            'username',
            'email',
            'role',
            'bio',
            'first_name',
            'last_name',
        )
        model = User

    def validate_username(self, value):
        if value == settings.RESERVED_NAME:
            raise serializers.ValidationError(
                f'Нельзя использовать юзернейм {settings.RESERVED_NAME}')
        return value


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=True)
    confirmation_code = serializers.CharField(max_length=150, required=True)

    def validate(self, data):
        if not User.objects.filter(username=data['username']).exists():
            raise exceptions.NotFound(
                f'Пользователь с юзернеймом {data["username"]} не найден')
        if 'username' or 'confirmation code' not in data:
            raise serializers.ValidationError(
                f'Не хватает данных в запросе. {data}')
        if data['username'] == settings.RESERVED_NAME:
            raise serializers.ValidationError(
                f'Нельзя использовать юзернейм {settings.RESERVED_NAME}')
