from django.urls import path
from .views import (
    UsuarioListView,
    UsuarioDetailView,
    UsuarioCreateView,
    UsuarioUpdateView,
    UsuarioDeleteView,
)

urlpatterns = [
    path('', UsuarioListView.as_view(), name='usuario_list'),
    path('<int:pk>/', UsuarioDetailView.as_view(), name='usuario_detail'),
    path('create/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('<int:pk>/update/', UsuarioUpdateView.as_view(), name='usuario_update'),
    path('<int:pk>/delete/', UsuarioDeleteView.as_view(), name='usuario_delete'),
]
