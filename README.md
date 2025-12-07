# Sistema Academia Dev Python

Sistema desenvolvido para o desafio técnico - Estágio Python/Django 2026.1

**Desenvolvedor:** Kaio Cesar De Sousa Pinheiro  
**Data:** 06/12/2025

## ⚠️ Sobre este projeto

Conforme orientação do desafio: "_Nenhuma das funcionalidades propostas no desafio é indispensável, então não deixe de enviar seu código, por mais incompleto que ele esteja_".

**Contexto:** Semana de provas na UFRN acabou ontem (05/12). Comecei o desafio hoje à tarde e implementei o máximo possível, priorizando demonstrar raciocínio e estrutura.

**Status:** Código implementado mas não testado completamente por limitação de tempo.

## Como rodar

```bash
git clone <repositorio>
cd academia-dev
docker-compose up --build
```

Deveria acessar:
- http://localhost:8000 (dashboard)
- http://localhost:8000/admin (admin/admin123)
- http://localhost:8000/api (API REST)

## Status: Código implementado mas não testado completamente

### O que implementei (arquivos existem):

**Backend:**
- ✅ Models: Aluno, Curso, Matricula com relacionamentos ForeignKey
- ✅ Serializers DRF com validações básicas
- ✅ ViewSets para API REST (CRUD completo)
- ✅ Views HTML para dashboard e histórico
- ✅ Admin Django configurado
- ✅ Endpoints de relatórios JSON

**Frontend:**
- ✅ Dashboard HTML com estatísticas
- ✅ Página de histórico do aluno
- ✅ CSS básico (não sou designer)

**Infraestrutura:**
- ✅ Docker e docker-compose
- ✅ PostgreSQL configurado
- ✅ Script de inicialização com dados de exemplo
- ✅ meu_database.sql com estrutura e queries

### Funcionalidades (em código):

**API REST:**
- `/api/alunos/` - CRUD completo
- `/api/cursos/` - CRUD completo
- `/api/matriculas/` - CRUD completo
- `/api/matriculas/{id}/marcar_paga/` - Marcar como paga
- `/api/matriculas/aluno/{id}/` - Listar por aluno

**Relatórios:**
- Dashboard com total de alunos, cursos, matrículas
- Resumo financeiro (pago vs pendente)
- Histórico detalhado do aluno
- 3 endpoints JSON de relatórios
- Consulta SQL bruta com JOIN e GROUP BY

**Admin:**
- Cadastro de alunos, cursos, matrículas
- Busca e filtros
- Ação para marcar múltiplas como pagas

## O que não ficou ideal

### 1. Não testei rodando
Principal limitação: implementei baseado em conhecimento da faculdade mas não rodei `docker-compose up` completamente. Pode ter pequenos erros que não identifiquei.

### 2. SQL bruto básico
Fiz JOIN com GROUP BY mas não consegui fazer agregações múltiplas (SUM + COUNT + CASE WHEN juntos). Tentei mas deu erro "column must appear in GROUP BY" e não consegui resolver.

### 3. Otimizações
Alguns lugares fazem N+1 queries (loop chamando métodos). Sei que não é ideal mas priorizei funcionar.

### 4. Validações simples
CPF só valida tamanho (11 dígitos), não os dígitos verificadores. Focando no prazo, implementei o básico.

### 5. Frontend básico
CSS muito simples. Meu foco é backend.

### 6. Sem testes automatizados
Não implementei testes unitários. Conheço o conceito mas não usei neste projeto.

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

## Decisão de enviar neste estado

Conforme o desafio: "_por mais incompleto que ele esteja, tudo será levado em consideração_".

Prioridades que segui:
1. **Estrutura** antes de perfeição - demonstrar arquitetura
2. **Conceitos** antes de testes - mostrar que entendo
3. **Honestidade** antes de inventar - transparência sobre limitações
4. **Enviar** antes de desistir - código incompleto > sem código

## O que aprendi implementando

- Estruturar projeto Django do zero
- Models com relacionamentos
- ViewSets e Serializers do DRF
- Consultas SQL com JOINs
- Docker multi-container
- Priorização sob pressão de tempo

## O que faria diferente com mais tempo

- Testar rodando completo e corrigir erros
- Implementar SQL com agregações complexas
- Otimizar queries (select_related, prefetch_related)
- Adicionar testes automatizados
- Melhorar validações (CPF completo)
- Frontend mais elaborado

## Observações

Este é meu primeiro projeto Django "completo" fora das disciplinas da UFRN. Usei como base o que aprendi nas aulas mas aplicando em um contexto real.

Semana de provas acabou ontem, comecei hoje (06/12) às 14h e implementei até agora (18h). Não é desculpa, é contexto.

Se houver erros que impeçam de rodar, posso corrigir. Se avançar no processo, posso explicar cada decisão técnica que tomei.

---

**Contato:**  
Kaio Cesar De Sousa Pinheiro  
Email: kaio.pinheiro.065@outlook.com  
Tel: +55 84 99183-0438  
LinkedIn: linkedin.com/in/kaio-cesar-de-sousa-pinheiro
