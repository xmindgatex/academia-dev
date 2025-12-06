#!/bin/bash

# espera o postgres
echo "Esperando banco..."
while ! nc -z db 5432; do
  sleep 0.5
done
echo "Banco conectado"

# migrations
python manage.py migrate

# cria superuser
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
    print('Admin criado')
END

# dados de exemplo
python manage.py shell << END
from core.models import Aluno, Curso, Matricula
from decimal import Decimal
from datetime import date, timedelta

if not Aluno.objects.exists():
    a1 = Aluno.objects.create(nome='Maria Silva', email='maria@email.com', cpf='12345678901', data_ingresso=date.today()-timedelta(days=30))
    a2 = Aluno.objects.create(nome='Joao Santos', email='joao@email.com', cpf='98765432100', data_ingresso=date.today()-timedelta(days=15))
    
    c1 = Curso.objects.create(nome='Python Basico', carga_horaria=40, valor_inscricao=Decimal('500.00'), status='ativo')
    c2 = Curso.objects.create(nome='Django Avancado', carga_horaria=60, valor_inscricao=Decimal('800.00'), status='ativo')
    
    Matricula.objects.create(aluno=a1, curso=c1, data_matricula=date.today()-timedelta(days=20), status_pagamento='pago')
    Matricula.objects.create(aluno=a1, curso=c2, data_matricula=date.today()-timedelta(days=10), status_pagamento='pendente')
    Matricula.objects.create(aluno=a2, curso=c1, data_matricula=date.today()-timedelta(days=5), status_pagamento='pendente')
    
    print('Dados criados')
END

exec "$@"
