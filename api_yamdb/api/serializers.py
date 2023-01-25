from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from reviews.models import Comment, Review, Title


# class ListTitleSerializer(serializers.ModelSerializer):
#     rating = serializers.IntegerField(
#         source='review__score__avg', read_only=True
#     )

class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для создания объекта класса Review."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    def validate(self, data):
        title_id = (
            self.context['request'].parser_context['kwargs']['title_id']
        )
        title = get_object_or_404(Title, pk=title_id)
        user = self.context['request'].user
        if (
            self.context['request'].method == 'POST'
            and Review.objects.filter(author=user, title=title).exists()
        ):
            raise ValidationError(
                'На одно произведение иожно оставить один отзыв.'
            )
        return data

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        read_only_fields = ('title',)


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для создания объекта класса Comment."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
        read_only_fields = ('review',)