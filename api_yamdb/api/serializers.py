from rest_framework import serializers
from reviews.models import User


class UserCreateSerializer(serializers.Serializer):
    """Сериализатор для создания объекта класса User."""

    username = serializers.RegexField(
        regex=r'^[\w.@+-]+$',
        max_length=150,
        required=True
    )
    email = serializers.EmailField(required=True, max_length=128)

    class Meta:
        fields = (
            'username', 'email'
        )

    def create(self, validated_data):
        user, _ = User.objects.get_or_create(**validated_data)
        return user

    def validate(self, data):
        if data.get('username') == 'me':
            raise serializers.ValidationError(
                'Использовать имя "me" запрещено'
            )
        if User.objects.filter(
                username=data.get('username'),
                email=data.get('email'),
        ).exists():
            return data

        username_exists = User.objects.filter(
            username=data.get('username'),
        ).exists()
        email_exists = User.objects.filter(email=data.get('email')).exists()

        if username_exists and email_exists:
            return data

        if username_exists:
            raise serializers.ValidationError(
                'Пользователь с таким username уже существует'
            )

        if email_exists:
            raise serializers.ValidationError(
                'Пользователь с таким email уже существует'
            )
        return data


class UserRecieveTokenSerializer(serializers.Serializer):
    """Сериализатор для объекта класса User при получении токена JWT."""

    username = serializers.RegexField(
        regex=r'^[\w.@+-]+$',
        max_length=150,
        required=True
    )
    confirmation_code = serializers.CharField(
        max_length=150,
        required=True
    )


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User."""

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )

    def validate_username(self, username):
        if username in 'me':
            raise serializers.ValidationError(
                'Использовать имя "me" запрещено'
            )
        return username
