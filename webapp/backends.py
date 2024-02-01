from django.contrib.auth.backends import ModelBackend
from .models import Account

class NamePasswordAuthBackend(ModelBackend):
    def authenticate(self, request, name=None, password=None, **kwargs):
        try:
            user = Account.objects.get(name=name)
        except Account.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None
