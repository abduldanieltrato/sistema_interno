from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Paciente, Analise, Resultado, Consumivel, Material

@receiver(post_migrate)
def setup_default_groups(sender, **kwargs):
    # Grupos
    recepcionista_group, _ = Group.objects.get_or_create(name='Recepcionista')
    tecnico_group, _ = Group.objects.get_or_create(name='Técnico')
    gestor_group, _ = Group.objects.get_or_create(name='Gestor')
    admin_group, _ = Group.objects.get_or_create(name='Administrador')

    # Permissões específicas
    paciente_ct = ContentType.objects.get_for_model(Paciente)
    analise_ct = ContentType.objects.get_for_model(Analise)
    resultado_ct = ContentType.objects.get_for_model(Resultado)
    consumivel_ct = ContentType.objects.get_for_model(Consumivel)
    material_ct = ContentType.objects.get_for_model(Material)

    # Permissões para recepcionista
    recepcionista_perms = [
        Permission.objects.get_or_create(codename='add_paciente', name='Pode adicionar paciente', content_type=paciente_ct)[0],
        Permission.objects.get_or_create(codename='change_paciente', name='Pode alterar paciente', content_type=paciente_ct)[0],
        Permission.objects.get_or_create(codename='view_paciente', name='Pode visualizar paciente', content_type=paciente_ct)[0],
        Permission.objects.get_or_create(codename='add_analise', name='Pode adicionar análise', content_type=analise_ct)[0],
        Permission.objects.get_or_create(codename='view_resultado', name='Pode visualizar resultados', content_type=resultado_ct)[0],
    ]
    recepcionista_group.permissions.set(recepcionista_perms)

    # Permissões para técnico (inclui as do recepcionista)
    tecnico_perms = recepcionista_perms + [
        Permission.objects.get_or_create(codename='add_resultado', name='Pode adicionar resultado', content_type=resultado_ct)[0],
        Permission.objects.get_or_create(codename='delete_paciente', name='Pode apagar paciente', content_type=paciente_ct)[0],
        Permission.objects.get_or_create(codename='delete_analise', name='Pode apagar análise', content_type=analise_ct)[0],
    ]
    tecnico_group.permissions.set(tecnico_perms)

    # Permissões para gestor (inclui as do técnico)
    gestor_perms = tecnico_perms + [
        Permission.objects.get_or_create(codename='add_consumivel', name='Pode adicionar consumível', content_type=consumivel_ct)[0],
        Permission.objects.get_or_create(codename='add_material', name='Pode adicionar material', content_type=material_ct)[0],
        Permission.objects.get_or_create(codename='change_consumivel', name='Pode alterar consumível', content_type=consumivel_ct)[0],
        Permission.objects.get_or_create(codename='change_material', name='Pode alterar material', content_type=material_ct)[0],
        Permission.objects.get_or_create(codename='delete_consumivel', name='Pode apagar consumível', content_type=consumivel_ct)[0],
        Permission.objects.get_or_create(codename='delete_material', name='Pode apagar material', content_type=material_ct)[0],
    ]
    gestor_group.permissions.set(gestor_perms)

    # Administrador tem todas as permissões
    admin_group.permissions.set(Permission.objects.all())
