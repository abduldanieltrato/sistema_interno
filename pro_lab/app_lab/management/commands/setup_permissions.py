from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from app_lab.models import (
    Paciente,
    Analise,
    Resultado,
    Consumivel,
    Material,
    BancoDeSangue,
)


class Command(BaseCommand):
    help = "Configura os grupos e permissões para o sistema"

    def handle(self, *args, **kwargs):
        # Definir grupos
        grupos = {
            "Recepcionista": {
                "permissions": [
                    "view_paciente",
                    "add_paciente",
                    "view_analise",
                    "view_resultado",
                ],
            },
            "Técnico": {
                "permissions": [
                    "view_paciente",
                    "add_paciente",
                    "change_paciente",
                    "delete_paciente",
                    "add_analise",
                    "change_analise",
                    "delete_analise",
                    "view_analise",
                    "add_resultado",
                    "change_resultado",
                    "delete_resultado",
                    "view_resultado",
                    "change_bancodesangue",
                ],
            },
            "Gestor": {
                "permissions": [
                    "view_paciente",
                    "add_paciente",
                    "change_paciente",
                    "delete_paciente",
                    "add_analise",
                    "change_analise",
                    "delete_analise",
                    "view_analise",
                    "add_resultado",
                    "change_resultado",
                    "delete_resultado",
                    "view_resultado",
                    "add_consumivel",
                    "change_consumivel",
                    "delete_consumivel",
                    "view_consumivel",
                    "add_material",
                    "change_material",
                    "delete_material",
                    "view_material",
                    "change_bancodesangue",
                ],
            },
            "Administrador": {
                "permissions": Permission.objects.all(),
            },
        }

        # Criar grupos e atribuir permissões
        for nome_grupo, config in grupos.items():
            grupo, created = Group.objects.get_or_create(name=nome_grupo)
            if "permissions" in config:
                for codename in config["permissions"]:
                    permission = Permission.objects.get(codename=codename)
                    grupo.permissions.add(permission)

        self.stdout.write(
            self.style.SUCCESS("Grupos e permissões configurados com sucesso!")
        )


from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = "Configura os grupos e permissões para o sistema"

    def handle(self, *args, **kwargs):
        # Definir grupos e permissões
        grupos = {
            "Recepcionista": {
                "permissions": [
                    "view_paciente",
                    "add_paciente",
                    "view_analise",
                    "view_resultado",
                ],
            },
            "Técnico": {
                "permissions": [
                    "view_paciente",
                    "add_paciente",
                    "change_paciente",
                    "delete_paciente",
                    "add_analise",
                    "change_analise",
                    "delete_analise",
                    "view_analise",
                    "add_resultado",
                    "change_resultado",
                    "delete_resultado",
                    "view_resultado",
                    "change_bancodesangue",
                ],
            },
            "Gestor": {
                "permissions": [
                    "view_paciente",
                    "add_paciente",
                    "change_paciente",
                    "delete_paciente",
                    "add_analise",
                    "change_analise",
                    "delete_analise",
                    "view_analise",
                    "add_resultado",
                    "change_resultado",
                    "delete_resultado",
                    "view_resultado",
                    "add_consumivel",
                    "change_consumivel",
                    "delete_consumivel",
                    "view_consumivel",
                    "add_material",
                    "change_material",
                    "delete_material",
                    "view_material",
                    "change_bancodesangue",
                ],
            },
            "Administrador": {
                "permissions": "all",  # Sinalizador para adicionar todas as permissões
            },
        }

        # Criar grupos e atribuir permissões
        for nome_grupo, config in grupos.items():
            grupo, created = Group.objects.get_or_create(name=nome_grupo)

            # Se o grupo é Administrador, adiciona todas as permissões
            if config["permissions"] == "all":
                all_permissions = Permission.objects.all()
                grupo.permissions.set(all_permissions)
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Todas as permissões atribuídas ao grupo {nome_grupo}."
                    )
                )
            else:
                # Atribuir permissões listadas no dicionário
                for codename in config["permissions"]:
                    try:
                        permission = Permission.objects.get(codename=codename)
                        grupo.permissions.add(permission)
                    except Permission.DoesNotExist:
                        self.stdout.write(
                            self.style.WARNING(
                                f"Permissão '{codename}' não encontrada e não foi atribuída ao grupo {nome_grupo}."
                            )
                        )

        self.stdout.write(
            self.style.SUCCESS("Grupos e permissões configurados com sucesso!")
        )
