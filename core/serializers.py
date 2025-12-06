from rest_framework import serializers
from .models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    total_devido = serializers.SerializerMethodField()
    total_pago = serializers.SerializerMethodField()
