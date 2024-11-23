from django.contrib import admin
from .models import (
    Usuario,
    Paciente,
    Analise,
    Resultado,
    Material,
    Consumivel,
    TipoSanguineo,
    BancoDeSangue,
    Auditoria, Exame, MaterialBase
)

@admin.register(Exame)
class ExameAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor_referencia', 'unidade_si', 'prazo_resultado', 'ativo', 'data_criacao')
    list_filter = ('ativo',)
    search_fields = ('nome', 'descricao', 'valor_referencia', 'unidade_si')
    ordering = ('nome',)
    list_editable = ('ativo',)

# Registro para o modelo Usuario
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_medico', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_medico', 'is_staff', 'is_active')

# Registro para o modelo Paciente
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'genero', 'telefone', 'residencia', 'nacionalidade', 'numero_identificacao', 'data_entrada', 'data_atualizacao')
    search_fields = ('nome', 'telefone', 'nacionalidade', 'data_nascimento')
    list_filter = ('genero', 'data_entrada', 'data_atualizacao', 'nacionalidade')

# Registro para o modelo Analise
@admin.register(Analise)
class AnaliseAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'paciente', 'status')
    search_fields = ('tipo', 'paciente__nome', 'status')
    list_filter = ('paciente__nome', 'status')

# Registro para o modelo Resultado
@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('analise', 'validado', 'validador', 'data_validacao', 'data_criacao')
    search_fields = ('analise__tipo', 'analise__paciente__nome')
    list_filter = ('validado', 'data_validacao')

# Registro para os modelos de materiais e consumíveis
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'estoque_minimo', 'validade', 'data_criacao')
    search_fields = ('nome',)
    list_filter = ('validade',)

@admin.register(Consumivel)
class ConsumivelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'estoque_minimo', 'validade', 'data_criacao')
    search_fields = ('nome',)
    list_filter = ('validade',)

# Registro para o modelo TipoSanguineo
@admin.register(TipoSanguineo)
class TipoSanguineoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descricao')
    search_fields = ('tipo',)

# Registro para o modelo BancoDeSangue
@admin.register(BancoDeSangue)
class BancoDeSangueAdmin(admin.ModelAdmin):
    list_display = ('tipo_sanguineo', 'quantidade_em_unidades', 'atualizado_em')
    search_fields = ('tipo_sanguineo__tipo',)
    list_filter = ('tipo_sanguineo',)

# Registro para o modelo Auditoria
@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'acao', 'objeto_afetado', 'data_acao')
    search_fields = ('usuario__username', 'acao', 'objeto_afetado')
    list_filter = ('data_acao',)

