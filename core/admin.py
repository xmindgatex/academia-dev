from django.contrib import admin
from .models import Aluno, Curso, Matricula

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'cpf', 'data_ingresso']
    search_fields = ['nome', 'email', 'cpf']
    list_filter = ['data_ingresso']


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'carga_horaria', 'valor_inscricao', 'status']
    search_fields = ['nome']
    list_filter = ['status']


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'curso', 'data_matricula', 'status_pagamento']
    search_fields = ['aluno__nome', 'curso__nome']
    list_filter = ['status_pagamento', 'data_matricula']
    
    actions = ['marcar_pagas']
    
    def marcar_pagas(self, request, queryset):
        qtd = queryset.update(status_pagamento='pago')
        self.message_user(request, f'{qtd} matriculas marcadas como pagas')
    
    marcar_pagas.short_description = 'Marcar como pagas'
