from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Предоставляет права на выполнение запросов
    только суперпользователю и администратору.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_admin or request.user.is_superuser)
