from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            (
                request.user and
                request.user.is_authenticated and
                obj.profile == request.user.profile
            )
        )

