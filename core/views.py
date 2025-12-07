from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, Count, Q
from django.db import connection
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Aluno, Curso, Matricula
from .serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer

# views html

def dashboard_view(request):
    # estatisticas
    total_alunos = Aluno.objects.count()
    cursos_ativos = Curso.objects.filter(status='ativo').count()
    
    # matriculas
    total_matriculas = Matricula.objects.count()
    matriculas_pagas = Matricula.objects.filter(status_pagamento='pago').count()
    matriculas_pendentes = Matricula.objects.filter(status_pagamento='pendente').count()
    
    # calcular valores
    # TODO: otimizar isso, ta fazendo muita query
    total_pago = 0
    total_pendente = 0
    for mat in Matricula.objects.all():
        if mat.status_pagamento == 'pago':
            total_pago += mat.curso.valor_inscricao
        else:
            total_pendente += mat.curso.valor_inscricao
    
    total_geral = total_pago + total_pendente
    
    alunos = Aluno.objects.all()[:10]
    
    context = {
        'total_alunos': total_alunos,
        'cursos_ativos': cursos_ativos,
        'total_matriculas': total_matriculas,
        'matriculas_pagas': matriculas_pagas,
        'matriculas_pendentes': matriculas_pendentes,
        'total_pago': total_pago,
        'total_pendente': total_pendente,
        'total_geral': total_geral,
        'alunos': alunos,
    }
    
    return render(request, 'core/dashboard.html', context)


def historico_aluno_view(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    matriculas = aluno.matriculas.all()
    
    total_pago = aluno.total_pago()
    total_devido = aluno.total_devido()
    total_geral = total_pago + total_devido
    
    context = {
        'dados': aluno,
        'matriculas': matriculas,
        'total_pago': total_pago,
        'total_devido': total_devido,
        'total_geral': total_geral,
    }
    
    return render(request, 'core/historico_aluno.html', context)


# api viewsets

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    
    def get_queryset(self):
        queryset = Aluno.objects.all()
        nome = self.request.query_params.get('nome', None)
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    def get_queryset(self):
        queryset = Curso.objects.all()
        status_filtro = self.request.query_params.get('status', None)
        if status_filtro:
            queryset = queryset.filter(status=status_filtro)
        return queryset


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    
    @action(detail=True, methods=['patch'])
    def marcar_paga(self, request, pk=None):
        matricula = self.get_object()
        matricula.marcar_paga()
        serializer = self.get_serializer(matricula)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='aluno/(?P<aluno_id>[^/.]+)')
    def por_aluno(self, request, aluno_id=None):
        matriculas = self.queryset.filter(aluno_id=aluno_id)
        serializer = self.get_serializer(matriculas, many=True)
        return Response(serializer.data)


# relatorios json

@api_view(['GET'])
def relatorio_matriculas_por_curso(request):
    cursos = Curso.objects.all()
    resultado = []
    
    for curso in cursos:
        total = curso.matriculas.count()
        pagas = curso.matriculas.filter(status_pagamento='pago').count()
        pendentes = curso.matriculas.filter(status_pagamento='pendente').count()
        
        resultado.append({
            'curso_id': curso.id,
            'curso_nome': curso.nome,
            'total_matriculas': total,
            'matriculas_pagas': pagas,
            'matriculas_pendentes': pendentes
        })
    
    return Response(resultado)


@api_view(['GET'])
def relatorio_devido_por_aluno(request):
    alunos = Aluno.objects.all()
    resultado = []
    
    for aluno in alunos:
        resultado.append({
            'aluno_id': aluno.id,
            'nome': aluno.nome,
            'email': aluno.email,
            'total_pago': float(aluno.total_pago()),
            'total_devido': float(aluno.total_devido()),
            'total_geral': float(aluno.total_pago() + aluno.total_devido())
        })
    
    return Response(resultado)


@api_view(['GET'])
def relatorio_pagamentos_pendentes(request):
    matriculas_pendentes = Matricula.objects.filter(status_pagamento='pendente')
    
    total = 0
    for mat in matriculas_pendentes:
        total += mat.curso.valor_inscricao
    
    lista = []
    for mat in matriculas_pendentes:
        lista.append({
            'matricula_id': mat.id,
            'aluno': mat.aluno.nome,
            'curso': mat.curso.nome,
            'valor': float(mat.curso.valor_inscricao),
            'data_matricula': mat.data_matricula.strftime('%Y-%m-%d')
        })
    
    return Response({
        'total_pendente': float(total),
        'quantidade': len(lista),
        'matriculas': lista
    })


# sql bruto
@api_view(['GET'])
def relatorio_sql_raw(request):
    # tentei fazer consulta mais complexa mas deu erro
    # consegui fazer o basico com join
    
    sql = """
        SELECT 
            a.id,
            a.nome,
            a.email,
            COUNT(m.id) as total_matriculas
        FROM core_aluno a
        LEFT JOIN core_matricula m ON a.id = m.aluno_id
        GROUP BY a.id, a.nome, a.email
        ORDER BY total_matriculas DESC
    """
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        colunas = [col[0] for col in cursor.description]
        resultados = []
        for linha in cursor.fetchall():
            resultado = dict(zip(colunas, linha))
            resultados.append(resultado)
    
    return Response({
        'info': 'Consulta SQL bruto',
        'resultados': resultados
    })
