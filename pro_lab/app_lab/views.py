from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Paciente
from .forms import AnaliseFormset

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
    )

from .forms import AnaliseForm, ExameForm, PacienteForm, ResultadoForm, UsuarioForm
from .models import Analise, Exame, Paciente, Resultado, Usuario

from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente, Exame, Analise
from .forms import CriarAnalisesForm

def detalhes_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id = paciente_id)
    analises = paciente.analises.all()  # Relaciona as análises com o paciente
    return render(request, 'detalhes_paciente.html', {'paciente': paciente, 'analises': analises})

def adicionar_analises(request, paciente_id):
    paciente = get_object_or_404(Paciente, id = paciente_id)

    if request.method == "POST":
        form = CriarAnalisesForm(request.POST)
        if form.is_valid():
            exames = form.cleaned_data['exames']
            descricao = form.cleaned_data['descricao']
            status = form.cleaned_data['status']

            # Criar uma análise para cada exame selecionado
            for exame in exames:
                Analise.objects.create(
                        paciente = paciente,
                        tipo = exame,
                        descricao = descricao,
                        status = status,
                        )
            return redirect('detalhes_paciente', paciente_id = paciente.id)  # Redireciona para os detalhes após salvar
    else:
        form = CriarAnalisesForm()

    return render(request, 'adicionar_analises.html', {'form': form, 'paciente': paciente})

@login_required
def gerenciar_analises(request, paciente_id):
    # Recupera o paciente ou retorna erro 404
    paciente = get_object_or_404(Paciente, id = paciente_id)

    # Inicializa o formset com a instância do paciente
    if request.method == "POST":
        formset = AnaliseFormset(request.POST, instance = paciente)
        if formset.is_valid():
            # Salva os exames adicionados para o paciente
            formset.save()
            return redirect("paciente_detail", pk = paciente_id)  # Redireciona para detalhes do paciente
    else:
        formset = AnaliseFormset(instance = paciente)

    return render(
            request,
            "app_lab/gerenciar_analises.html",
            {"paciente": paciente, "formset": formset},
            )

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "app_lab/index.html"

# Usuários
# Lista de usuários
class UsuarioListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Usuario
    template_name = "app_lab/usuario/usuario_list.html"
    context_object_name = "usuarios"
    permission_required = "app_lab.view_usuario"

# Detalhes de um usuário
class UsuarioDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Usuario
    template_name = "app_lab/usuario/usuario_detail.html"
    context_object_name = "usuario"
    permission_required = "app_lab.view_usuario"

# Criar um novo usuário
class UsuarioCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "app_lab/usuario/usuario_form.html"
    success_url = reverse_lazy("usuario_list")
    permission_required = "app_lab.add_usuario"

# Atualizar um usuário existente
class UsuarioUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = "app_lab/usuario/usuario_form.html"
    success_url = reverse_lazy("usuario_list")
    permission_required = "app_lab.change_usuario"

# Deletar um usuário
class UsuarioDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Usuario
    template_name = "app_lab/usuario/usuario_confirm_delete.html"
    success_url = reverse_lazy("usuario_list")
    permission_required = "app_lab.delete_usuario"

# Pacientes


class PacienteListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Paciente
    template_name = "app_lab/paciente/paciente_list.html"
    context_object_name = "pacientes"
    permission_required = "app_lab.view_paciente"

    # Sobrescrevendo o método get_queryset para ordenar pela data de entrada de forma decrescente
    def get_queryset(self):
        return Paciente.objects.all().order_by(
                "-data_entrada"
                )  # Ordena os pacientes pelo campo data_entrada (decrescente)

class PacienteDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Paciente
    template_name = "app_lab/paciente/paciente_detail.html"
    permission_required = "app_lab/paciente/paciente_detail"

class PacienteCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "app_lab/paciente/paciente_form.html"
    success_url = reverse_lazy("paciente_list")
    permission_required = "app_lab.add_paciente"

class PacienteUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "app_lab/paciente/paciente_form.html"
    success_url = reverse_lazy("paciente_list")
    permission_required = "app_lab.change_paciente"

class PacienteDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Paciente
    template_name = "app_lab/paciente/paciente_confirm_delete.html"
    success_url = reverse_lazy("paciente_list")
    permission_required = "app_lab.delete_paciente"

# Análises
class AnaliseListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Analise
    template_name = "app_lab/analise/analise_list.html"
    context_object_name = "analises"
    permission_required = "app_lab.view_analise"

class AnaliseDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Analise
    template_name = "app_lab/analise/analise_detail.html"
    context_object_name = "analise"
    permission_required = "app_lab.view_analise"

class AnaliseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Analise
    form_class = AnaliseForm
    template_name = "app_lab/analise/analise_form.html"
    success_url = reverse_lazy("analise_list")
    permission_required = "app_lab.add_analise"

class AnaliseUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Analise
    form_class = AnaliseForm
    template_name = "app_lab/analise/analise_form.html"
    success_url = reverse_lazy("analise_list")
    permission_required = "app_lab.change_analise"

class AnaliseDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Analise
    template_name = "app_lab/analise/analise_confirm_delete.html"
    success_url = reverse_lazy("analise_list")
    permission_required = "app_lab.delete_analise"

# Resultados
class ResultadoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Resultado
    template_name = "app_lab/resultado/resultado_list.html"
    context_object_name = "resultados"
    permission_required = "app_lab.view_resultado"

class ResultadoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Resultado
    template_name = "app_lab/resultado/resultado_detail.html"
    context_object_name = "resultado"
    permission_required = "app_lab.view_resultado"

class ResultadoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Resultado
    form_class = ResultadoForm
    template_name = "app_lab/resultado/resultado_form.html"
    success_url = reverse_lazy("resultado_list")
    permission_required = "app_lab.add_resultado"

class ResultadoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Resultado
    form_class = ResultadoForm
    template_name = "app_lab/resultado/resultado_form.html"
    success_url = reverse_lazy("resultado_list")
    permission_required = "app_lab.change_resultado"

class ResultadoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Resultado
    template_name = "app_lab/resultado/resultado_confirm_delete.html"
    success_url = reverse_lazy("resultado_list")
    permission_required = "app_lab.delete_resultado"

# Exames
class ExameListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Exame
    template_name = "app_lab/exame/exame_list.html"
    context_object_name = "exames"
    permission_required = "app_lab.view_exame"

class ExameDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Exame
    template_name = "app_lab/exame/exame_detail.html"
    context_object_name = "exame"
    permission_required = "app_lab.view_exame"

class ExameCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Exame
    form_class = ExameForm
    template_name = "app_lab/exame/exame_form.html"
    success_url = reverse_lazy("exame_list")
    permission_required = "app_lab.add_exame"

class ExameUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Exame
    form_class = ExameForm
    template_name = "app_lab/exame/exame_form.html"
    success_url = reverse_lazy("exame_list")
    permission_required = "app_lab.change_exame"

class ExameDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Exame
    template_name = "app_lab/exame/exame_confirm_delete.html"
    success_url = reverse_lazy("exame_list")
    permission_required = "app_lab.delete_exame"

from django.shortcuts import render
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from .models import Analise, Paciente
from django.db.models import Q

# Relatório de todas as análises feitas
def relatorio_analises(request):
    analises = Analise.objects.all().order_by('-data_realizacao')  # Ordena por data de realização
    return render(request, 'relatorio_analises.html', {'analises': analises})

# Relatório de pacientes atendidos
def relatorio_pacientes_atendidos(request):
    pacientes_atendidos = Paciente.objects.filter(analises__isnull = False).distinct()
    return render(request, 'relatorio_pacientes_atendidos.html', {'pacientes': pacientes_atendidos})

# Relatório de análises diárias
def relatorio_analises_diarias(request):
    today = timezone.now().date()
    analises_diarias = Analise.objects.filter(data_realizacao__date = today)
    return render(request, 'relatorio_analises_diarias.html', {'analises': analises_diarias})

# Relatório de análises semanais
def relatorio_analises_semanais(request):
    today = timezone.now().date()
    start_of_week = today - timedelta(days = today.weekday())  # Calcula o início da semana
    analises_semanais = Analise.objects.filter(data_realizacao__date__gte = start_of_week)
    return render(request, 'relatorio_analises_semanais.html', {'analises': analises_semanais})

# Relatório de análises mensais
def relatorio_analises_mensais(request):
    today = timezone.now().date()
    start_of_month = today.replace(day = 1)  # Calcula o primeiro dia do mês
    analises_mensais = Analise.objects.filter(data_realizacao__date__gte = start_of_month)
    return render(request, 'relatorio_analises_mensais.html', {'analises': analises_mensais})

# Relatório de pacientes atendidos por mês
def relatorio_pacientes_atendidos_mes(request):
    today = timezone.now().date()
    start_of_month = today.replace(day = 1)
    pacientes_atendidos_mes = Paciente.objects.filter(
            analises__data_realizacao__gte = start_of_month
            ).distinct()
    return render(request, 'relatorio_pacientes_atendidos_mes.html', {'pacientes': pacientes_atendidos_mes})
