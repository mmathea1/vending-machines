from rest_framework import permissions


class IsMachineManagerPermission(permissions.BasePermission):
    def has_permission(self, request, context):
        vending_machine = context.get('vending_machine')
        user = request.user
        return vending_machine.manager == user
