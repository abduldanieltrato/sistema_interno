from django import forms
from django.forms import inlineformset_factory
from django.utils.timezone import now

from .models import (
    Analise,
    Auditoria,
    BancoDeSangue,
    Consumivel,
    Exame,
    Material,
    Paciente,
    Resultado,
    TipoSanguineo,
    Usuario,
    )

from django import forms
from .models import Exame

class CriarAnalisesForm(forms.Form):
    exames = forms.ModelMultipleChoiceField(
            queryset = Exame.objects.all(),
            widget = forms.CheckboxSelectMultiple,  # Apresenta os exames como checkboxes
            required = True,
            )
    descricao = forms.CharField(
            widget = forms.Textarea,
            required = False,
            help_text = "Descrição adicional (opcional)."
            )
    status = forms.ChoiceField(
            choices = [
                    ("pendente", "Pendente"),
                    ("em andamento", "Em Andamento"),
                    ("concluída", "Concluída"),
                    ],
            initial = "pendente",
            required = True,
            )

# Formulário para o modelo Exame
class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = [
                "nome",
                "descricao",
                "valor_referencia",
                "unidade_si",
                "prazo_resultado",
                "ativo",
                ]

# Formulário para o modelo Usuario
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
                "username",
                "first_name",
                "last_name",
                "email",
                "is_medico",
                "password",
                ]
        widgets = {
                "password": forms.PasswordInput(),
                }

# Formulário para o modelo Paciente
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
                "nome",
                "data_nascimento",
                "genero",
                "telefone",
                "residencia",
                "nacionalidade",
                "numero_identificacao",
                "exames",
                ]

    def clean_data_nascimento(self):
        data = self.cleaned_data["data_nascimento"]
        if data > now().date():
            raise forms.ValidationError("A data de nascimento não pode ser no futuro.")
        return data

# Formulário para o modelo Analise
class AnaliseForm(forms.ModelForm):
    class Meta:
        model = Analise
        fields = ["paciente", "tipo", "descricao", "status"]
        widgets = {
                "paciente" : forms.Select(attrs = {"class": "form-control"}),
                "tipo"     : forms.Select(attrs = {"class": "form-control"}),
                "descricao": forms.Textarea(attrs = {"class": "form-control"}),
                "status"   : forms.Select(attrs = {"class": "form-control"}),
                }

# Formulário para o modelo Resultado
class ResultadoForm(forms.ModelForm):
    class Meta:
        model = Resultado
        fields = ["analise", "dados", "validado", "validador", "data_validacao"]

# Formulário para o modelo Material
class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ["nome", "quantidade", "estoque_minimo", "validade", "descricao"]

    def clean(self):
        cleaned_data = super().clean()
        quantidade = cleaned_data.get("quantidade")
        estoque_minimo = cleaned_data.get("estoque_minimo")
        if quantidade < estoque_minimo:
            raise forms.ValidationError(
                    "A quantidade não pode ser menor que o estoque mínimo."
                    )
        return cleaned_data

# Formulário para o modelo Consumivel
class ConsumivelForm(forms.ModelForm):
    class Meta:
        model = Consumivel
        fields = ["nome", "quantidade", "estoque_minimo", "validade", "descricao"]

# Formulário para o modelo TipoSanguineo
class TipoSanguineoForm(forms.ModelForm):
    class Meta:
        model = TipoSanguineo
        fields = ["tipo", "descricao"]

# Formulário para o modelo BancoDeSangue
class BancoDeSangueForm(forms.ModelForm):
    class Meta:
        model = BancoDeSangue
        fields = ["tipo_sanguineo", "quantidade_em_unidades"]

# Formulário para o modelo Auditoria (geralmente apenas leitura, mas incluído caso seja necessário)
class AuditoriaForm(forms.ModelForm):
    class Meta:
        model = Auditoria
        fields = ["usuario", "acao", "objeto_afetado"]

AnaliseFormset = inlineformset_factory(
        Paciente,
        Analise,
        form = AnaliseForm,
        extra = 1,  # Quantidade inicial de formulários exibidos
        can_delete = True,  # Permitir exclusão de análises
        )
