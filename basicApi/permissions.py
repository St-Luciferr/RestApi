from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an article to edit it.
    """
    def has_object_permission(self, request, view, obj):
        '''
        Give Read permissions to all request and
        check if request is from owner for edit
        '''
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user