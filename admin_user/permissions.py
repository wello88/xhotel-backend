# permissions.py
from rest_framework import permissions

class IsSuperuserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow GET, HEAD, and OPTIONS requests for all users.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Restrict other HTTP methods to superusers only.
        return request.user and request.user.is_superuser
