from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

# models do sistema

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_ingresso = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
    
    def total_devido(self):
        # soma as matriculas pendentes
        total = 0
        for m in self.matriculas.filter(status_pagamento='pendente'):
            total += m.curso.valor_inscricao
        return total
    
    def total_pago(self):
        total = 0
        for m in self.matriculas.filter(status_pagamento='pago'):
            total += m.curso.valor_inscricao
        return total


class Curso(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ]
    
    nome = models.CharField(max_length=200)
    carga_horaria = models.IntegerField()
    valor_inscricao = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
    
    def total_matriculas(self):
        return self.matriculas.count()


class Matricula(models.Model):
    STATUS_PAGAMENTO = [
        ('pago', 'Pago'),
        ('pendente', 'Pendente'),
    ]
    
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='matriculas')
    data_matricula = models.DateField()
    status_pagamento = models.CharField(max_length=10, choices=STATUS_PAGAMENTO, default='pendente')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Matrícula'
        verbose_name_plural = 'Matrículas'
        ordering = ['-data_matricula']
        unique_together = ['aluno', 'curso']
    
    def __str__(self):
        return f"{self.aluno.nome} - {self.curso.nome}"
    
    def marcar_paga(self):
        self.status_pagamento = 'pago'
        self.save()
