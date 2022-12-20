from rest_framework.permissions import BasePermission
from rest_framework import permissions
class is_Alumno(BasePermission):
    def has_permission(self, request, view):
        admin_permission=bool(request.user and request.user.is_Alumno)
        return request.method == admin_permission
        

class is_Profesor(BasePermission):
    def has_permission(self, request, view):
        admin_permission=bool(request.user and request.user.is_Profesor)
        return request.method == admin_permission

class is_AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        admin_permission= bool(request.user and request.user.is_staff)
        return request.method == "GET"  or admin_permission