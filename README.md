# Sistema Academia Dev Python

Sistema desenvolvido para o desafio técnico - Estágio Python/Django 2026.1

**Desenvolvedor:** Kaio Cesar  
**Tempo:** ~6 horas (05-06/12)  
**Data:** Dezembro 2025

## Como rodar

```bash
git clone <repositorio>
cd academia-dev
docker-compose up --build
```

Acesse:
- Sistema: http://localhost:8000
- Admin: http://localhost:8000/admin (admin/admin123)
- API: http://localhost:8000/api

## O que foi implementado

### Completo (~75%)

✅ Models (Aluno, Curso, Matricula)  
✅ Admin Django configurado  
✅ API REST básica (GET, POST, PATCH, DELETE)  
✅ Dashboard HTML com estatísticas  
✅ Histórico do aluno  
✅ Relatórios JSON (3 endpoints)  
✅ Docker funcionando  
✅ Dados de exemplo automáticos  

### Parcial (~15%)

⚠️ SQL Bruto: consegui fazer JOIN com GROUP BY mas tive dificuldade com agregações múltiplas (SUM + COUNT + CASE WHEN juntos). Erro "column must appear in GROUP BY". Entendo o conceito mas preciso estudar mais.

⚠️ Otimização: sei que em alguns lugares tô fazendo N+1 queries (loop chamando métodos). Pesquisei sobre select_related() mas não consegui aplicar.

⚠️ Validações: CPF só verifica tamanho, não os dígitos verificadores. Email só usa filter_var básico.

### Não implementado (~10%)

❌ Testes automatizados: focando no prazo, priorizei funcionalidades. Tenho experiência com testes manuais (trabalho) mas não com automatizados.

❌ Funcionalidades extras: paginação, filtros avançados, edição inline no admin.

## Estrutura

```
academia-dev/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── manage.py
├── meu_database.sql
├── academia/
│   ├── settings.py
│   └── urls.py
└── core/
    ├── models.py
    ├── views.py
    ├── serializers.py
    ├── admin.py
    └── templates/
```

## Tecnologias

- Python 3.11
- Django 5.0
- Django REST Framework 3.14
- PostgreSQL 15
- Docker & Docker Compose

## Dificuldades

### 1. SQL complexo
Tentei fazer query com múltiplas agregações mas travei. Pesquisei Stack Overflow e documentação PostgreSQL mas não consegui resolver o GROUP BY com várias funções agregadas.

### 2. Otimização de queries
Percebi que alguns trechos fazem muitas queries (N+1 problem). Sei que existe solução mas não consegui implementar no prazo.

### 3. Frontend
CSS bem básico. Não sou designer então deixei funcional mas simples.

## O que aprendi

- Estruturar projeto Django do zero
- ViewSets do DRF
- Docker multi-container
- Relacionamentos ForeignKey
- SQL bruto com cursor()
- Priorizar quando tem prazo

## Se tivesse mais tempo

- Implementar testes (pelo menos models)
- Corrigir SQL complexo
- Otimizar queries N+1
- Melhorar CSS
- Adicionar paginação

## Observações

Primeiro projeto Django "completo" fora da faculdade. Tem pontos de melhoria mas aprendi muito.

Comecei hoje à tarde (05/12) após o afazeres e continuei hoje. Estava com semana corrida na faculdade.
---

**Contato:**  
Kaio Cesar De Sousa Pinheiro  
kaio.pinheiro.065@outlook.com  
linkedin.com/in/kaio-cesar-de-sousa-pinheiro
