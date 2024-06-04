from rest_framework.permissions import BasePermission


class IsSurveyor(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(id='1').exists()


class IsAnalyst(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(id='2').exists()


class IsChannelizer(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(id='3').exists()


class IsAdministrator(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(id='4').exists()
