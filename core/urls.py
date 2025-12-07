from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'alunos', views.AlunoViewSet, basename='aluno')
router.register(r'cursos', views.CursoViewSet, basename='curso')
router.register(r'matriculas', views.MatriculaViewSet, basename='matricula')

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('historico/<int:aluno_id>/', views.historico_aluno_view, name='historico'),
    
    path('api/', include(router.urls)),
    
    path('api/relatorios/matriculas-por-curso/', views.relatorio_matriculas_por_curso),
    path('api/relatorios/devido-por-aluno/', views.relatorio_devido_por_aluno),
    path('api/relatorios/pagamentos-pendentes/', views.relatorio_pagamentos_pendentes),
    path('api/relatorios/alunos-cursos-raw/', views.relatorio_sql_raw),
]
