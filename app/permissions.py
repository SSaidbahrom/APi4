from rest_framework.permissions import BasePermission
from datetime import datetime

class ISCayomBlocked(BasePermission):
    def has_permission(self, request, view):
        if request.user.username == 'ismoil':
            return False
        return True 

class WorkDay(BasePermission):
    def has_permission(self, request, view):
        now = datetime.now()
        today = now.weekday()
        hour = now.hour

        return 0 <= today <= 5 and 2 <= hour <= 6
