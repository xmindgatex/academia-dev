from rest_framework import serializers
from .models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    total_devido = serializers.SerializerMethodField()
    total_pago = serializers.SerializerMethodField()
 class Meta:
        model = Aluno
        fields = ['id', 'nome', 'email', 'cpf', 'data_ingresso', 'total_devido', 'total_pago']
    
    def get_total_devido(self, obj):
        return obj.total_devido()
    
    def get_total_pago(self, obj):
        return obj.total_pago()
    
    def validate_cpf(self, value):
        # validacao simples
        # TODO: implementar validacao completa com digitos verificadores
        if len(value) != 11:
            raise serializers.ValidationError("CPF precisa ter 11 digitos")
        if not value.isdigit():
            raise serializers.ValidationError("CPF so pode ter numeros")
        return value


class CursoSerializer(serializers.ModelSerializer):
    total_matriculas = serializers.SerializerMethodField()
    
    class Meta:
        model = Curso
        fields = ['id', 'nome', 'carga_horaria', 'valor_inscricao', 'status', 'total_matriculas']
    
    def get_total_matriculas(self, obj):
        return obj.total_matriculas()


class MatriculaSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.CharField(source='aluno.nome', read_only=True)
    curso_nome = serializers.CharField(source='curso.nome', read_only=True)
    valor_curso = serializers.DecimalField(source='curso.valor_inscricao', max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = Matricula
        fields = ['id', 'aluno', 'aluno_nome', 'curso', 'curso_nome', 'valor_curso', 'data_matricula', 'status_pagamento']
    
    def validate(self, data):
        curso = data.get('curso')
        if curso and curso.status != 'ativo':
            raise serializers.ValidationError({'curso': 'Nao pode matricular em curso inativo'})
        return data
