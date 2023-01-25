# from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from reviews.models import Review, Title

from .permissions import IsSuperUserIsAdminIsModeratorIsAuthor
from .serializers import (CommentSerializer,
                          ReviewSerializer)


# class TitleViewSet(viewsets.ModelViewSet):
#     queryset = Title.objects.annotate(
#         Avg("review__score")
#     ).order_by("name")

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsSuperUserIsAdminIsModeratorIsAuthor,)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.review.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsSuperUserIsAdminIsModeratorIsAuthor]

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)