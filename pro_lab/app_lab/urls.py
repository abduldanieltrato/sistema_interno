from app_lab.views import (
    AnaliseCreateView, AnaliseDeleteView, AnaliseDetailView, AnaliseListView, AnaliseUpdateView, ExameCreateView,
    ExameDeleteView, ExameDetailView, ExameListView, ExameUpdateView, gerenciar_analises, IndexView, PacienteCreateView,
    PacienteDeleteView, PacienteDetailView, PacienteListView, PacienteUpdateView, ResultadoCreateView,
    ResultadoDeleteView, ResultadoDetailView, ResultadoListView, ResultadoUpdateView, UsuarioCreateView,
    UsuarioDeleteView, UsuarioDetailView, UsuarioListView, UsuarioUpdateView,
    )
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
        # Página inicial
        path("", IndexView.as_view(), name = "index"),
        path('relatorio/analises/', views.relatorio_analises, name = 'relatorio_analises'),
        path(
                'relatorio/pacientes_atendidos/', views.relatorio_pacientes_atendidos,
                name = 'relatorio_pacientes_atendidos'
                ),
        path('relatorio/analises_diarias/', views.relatorio_analises_diarias, name = 'relatorio_analises_diarias'),
        # Autenticação
        path("login/", auth_views.LoginView.as_view(), name = "login"),
        path("logout/", auth_views.LogoutView.as_view(next_page = "/login/"), name = "logout"),

        # Usuários
        path("usuarios/", UsuarioListView.as_view(), name = "usuario_list"),
        path("usuarios/novo/", UsuarioCreateView.as_view(), name = "usuario_create"),
        path("usuarios/<int:pk>/", UsuarioDetailView.as_view(), name = "usuario_detail"),
        path("usuarios/<int:pk>/editar/", UsuarioUpdateView.as_view(), name = "usuario_update"),
        path("usuarios/<int:pk>/deletar/", UsuarioDeleteView.as_view(), name = "usuario_delete"),

        # Pacientes
        path('paciente/<int:paciente_id>/', views.detalhes_paciente, name = 'detalhes_paciente'),
        path('paciente/<int:paciente_id>/analises/', views.adicionar_analises, name = 'adicionar_analises'),

        path("pacientes/", PacienteListView.as_view(), name = "paciente_list"),
        path("pacientes/novo/", PacienteCreateView.as_view(), name = "paciente_create"),
        path("pacientes/<int:pk>/", PacienteDetailView.as_view(), name = "paciente_detail"),
        path("pacientes/<int:pk>/editar/", PacienteUpdateView.as_view(), name = "paciente_update"),
        path("pacientes/<int:pk>/deletar/", PacienteDeleteView.as_view(), name = "paciente_delete"),
        path("pacientes/<int:paciente_id>/analises/", gerenciar_analises, name = "gerenciar_analises"),

        # Análises
        path("analises/", AnaliseListView.as_view(), name = "analise_list"),
        path("analises/novo/", AnaliseCreateView.as_view(), name = "analise_create"),
        path("analises/<int:pk>/", AnaliseDetailView.as_view(), name = "analise_detail"),
        path("analises/<int:pk>/editar/", AnaliseUpdateView.as_view(), name = "analise_update"),
        path("analises/<int:pk>/deletar/", AnaliseDeleteView.as_view(), name = "analise_delete"),

        # Resultados
        path("resultados/", ResultadoListView.as_view(), name = "resultado_list"),
        path("resultados/novo/", ResultadoCreateView.as_view(), name = "resultado_create"),
        path("resultados/<int:pk>/", ResultadoDetailView.as_view(), name = "resultado_detail"),
        path("resultados/<int:pk>/editar/", ResultadoUpdateView.as_view(), name = "resultado_update"),
        path("resultados/<int:pk>/deletar/", ResultadoDeleteView.as_view(), name = "resultado_delete"),

        # Exames
        path("exames/", ExameListView.as_view(), name = "exame_list"),
        path("exames/novo/", ExameCreateView.as_view(), name = "exame_create"),
        path("exames/<int:pk>/", ExameDetailView.as_view(), name = "exame_detail"),
        path("exames/<int:pk>/editar/", ExameUpdateView.as_view(), name = "exame_update"),
        path("exames/<int:pk>/deletar/", ExameDeleteView.as_view(), name = "exame_delete"),
        ]
