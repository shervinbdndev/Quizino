from typing import Self
from django.http.request import HttpRequest
from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    def has_permission(self: Self, request: HttpRequest, view) -> bool:
        if (request.user.is_staff):
            return True
        else:
            return False