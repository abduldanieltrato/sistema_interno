from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from app_lab.models import Paciente, Analise, Resultado, Material, Consumivel

# Criação dos grupos
recepcionista, _ = Group.objects.get_or_create(name="Recepcionista")
tecnico, _ = Group.objects.get_or_create(name="Técnico")
gestor, _ = Group.objects.get_or_create(name="Gestor")
administrador, _ = Group.objects.get_or_create(name="Administrador")

# Permissões para Recepcionistas
recepcionista.permissions.set([
    Permission.objects.get(codename="add_paciente"),
    Permission.objects.get(codename="view_paciente"),
    Permission.objects.get(codename="view_resultado"),
    Permission.objects.get(codename="add_analise"),
])

# Permissões para Técnicos
tecnico.permissions.set([
    *recepcionista.permissions.all(),
    Permission.objects.get(codename="add_resultado"),
    Permission.objects.get(codename="delete_paciente"),
    Permission.objects.get(codename="delete_resultado"),
    Permission.objects.get(codename="delete_analise"),
])

# Permissões para Gestores
gestor.permissions.set([
    *tecnico.permissions.all(),
    Permission.objects.get(codename="add_consumivel"),
    Permission.objects.get(codename="add_material"),
    Permission.objects.get(codename="delete_consumivel"),
    Permission.objects.get(codename="delete_material"),
])

# Permissões para Administradores (todas as permissões)
administrador.permissions.set(Permission.objects.all())
