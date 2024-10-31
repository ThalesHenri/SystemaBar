from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from .models import GarcomModel, AdminModel, CozinhaModel

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Tenta buscar o usuário por email (ajuste conforme necessário para outras entidades)
            user = GarcomModel.objects.get(email=username)
        except GarcomModel.DoesNotExist:
            try:
                user = AdminModel.objects.get(email=username)
            except AdminModel.DoesNotExist:
                return None

        # Verifica a senha
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return GarcomModel.objects.get(pk=user_id)
        except GarcomModel.DoesNotExist:
            try:
                return AdminModel.objects.get(pk=user_id)
            except AdminModel.DoesNotExist:
                return None
                

