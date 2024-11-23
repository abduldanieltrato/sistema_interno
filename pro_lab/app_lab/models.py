from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField


# Usuário personalizado
class Usuario(AbstractUser):
    is_medico = models.BooleanField(default=False)


class Exame(models.Model):
    nome = models.CharField(max_length=255, unique=True)  # Nome do exame
    descricao = models.TextField(blank=True, null=True)  # Detalhes sobre o exame
    valor_referencia = models.CharField(
        max_length=255, help_text="Exemplo: 4.5 - 6.0"
    )  # Valor de referência
    unidade_si = models.CharField(
        max_length=50, help_text="Exemplo: g/dL, mmol/L"
    )  # Unidade no sistema internacional
    prazo_resultado = models.PositiveIntegerField(
        help_text="Prazo para resultado em dias"
    )  # Prazo de entrega do resultado
    ativo = models.BooleanField(default=True)  # Indica se o exame está disponível
    data_criacao = models.DateTimeField(
        auto_now_add=True
    )  # Data de criação do registro
    data_atualizacao = models.DateTimeField(auto_now=True)  # Data da última atualização

    class Meta:
        verbose_name_plural = "Exames"

    def __str__(self):
        return self.nome


# Modelo de Paciente
class Paciente(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    genero = models.CharField(
        max_length=10,
        choices=[
            ("Masculino", "Masculino"),
            ("Feminino", "Feminino"),
            ("Outro", "Outro"),
        ],
    )
    telefone = models.CharField(max_length=15)
    residencia = models.CharField(max_length=100, blank=True, null=True)
    nacionalidade = CountryField(
        blank=False, null=False, default="MZ"
    )  # Exemplo: Moçambique como padrão
    numero_identificacao = models.CharField(max_length=20, blank=True, null=True)
    exames = models.ManyToManyField(
        "Exame", blank=True
    )  # Relacionamento com o modelo Exame
    data_entrada = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.nome


# Modelo de Análise
class Analise(models.Model):
    paciente = models.ForeignKey(
        Paciente, on_delete=models.CASCADE, related_name="analises"
    )
    tipo = models.ForeignKey(Exame, on_delete=models.CASCADE)
    descricao = models.TextField(blank=True)
    data_realizacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pendente", "Pendente"),
            ("em andamento", "Em Andamento"),
            ("concluída", "Concluída"),
        ],
        default="pendente",
    )

    class Meta:
        verbose_name_plural = "Análises"

    def __str__(self):
        return f"{self.tipo} - {self.paciente.nome}"


# Modelo de Resultado
class Resultado(models.Model):
    analise = models.ForeignKey(
        Analise, on_delete=models.CASCADE, related_name="resultados"
    )
    dados = models.TextField()
    validado = models.BooleanField(default=False)
    validador = models.ForeignKey(
        Usuario, on_delete=models.SET_NULL, null=True, blank=True
    )
    data_validacao = models.DateTimeField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Resultados"

    def __str__(self):
        return f"Resultado de {self.analise.tipo} para {self.analise.paciente.nome}"


# Modelo de Material e Consumível
class MaterialBase(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    estoque_minimo = models.PositiveIntegerField(default=10)
    validade = models.DateField()
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Materiais e Consumíveis"
        abstract = True

    def __str__(self):
        return f"{self.nome} - Estoque: {self.quantidade} - Validade: {self.validade}"


class Material(MaterialBase):
    pass


class Consumivel(MaterialBase):
    pass


# Modelo de Banco de Sangue
class TipoSanguineo(models.Model):
    tipo = models.CharField(
        max_length=3,
        choices=[
            ("A-", "A-"),
            ("A+", "A+"),
            ("B-", "B-"),
            ("B+", "B+"),
            ("AB-", "AB-"),
            ("AB+", "AB+"),
            ("O-", "O-"),
            ("O+", "O+"),
        ],
    )
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Tipos Sanguineos"

    def __str__(self):
        return self.tipo


class BancoDeSangue(models.Model):
    tipo_sanguineo = models.ForeignKey(TipoSanguineo, on_delete=models.CASCADE)
    quantidade_em_unidades = models.PositiveIntegerField()
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Bancos de Sangue"

    def __str__(self):
        return f"{self.tipo_sanguineo.tipo} - {self.quantidade_em_unidades} Unidades"


# Modelo de Auditoria
class Auditoria(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    acao = models.CharField(max_length=255)
    objeto_afetado = models.CharField(max_length=255)
    data_acao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Auditorias"

    def __str__(self):
        return f"{self.usuario} {self.acao} em {self.data_acao}"
