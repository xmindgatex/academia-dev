# Sistema de Gestão - Academia Dev Python

Sistema desenvolvido para o desafio técnico da vaga de estágio Python/Django 2026.1

**Desenvolvedor:** Kaio Cesar  
**Tempo investido:** Aproximadamente 18 horas  
**Data:** Dezembro 2025

## Como rodar o projeto

```bash
# 1. Clonar o repositório
git clone <repositorio>
cd academia-dev

# 2. Subir com docker
docker-compose up --build

# 3. Acessar
# Frontend: http://localhost:8000
# Admin: http://localhost:8000/admin
# API: http://localhost:8000/api
```

**Credenciais do admin:** admin / admin123 (criadas automaticamente)

## O que foi implementado

### Funcionalidades principais (funcionando)

✅ **Models:**
- Aluno (nome, email, cpf, data de ingresso)
- Curso (nome, carga horária, valor, status)
- Matricula (relaciona aluno e curso, controla pagamento)

✅ **Admin do Django:**
- Cadastro e listagem de alunos, cursos e matrículas
- Busca e filtros básicos
- Ação para marcar múltiplas matrículas como pagas

✅ **API REST:**
- CRUD completo de alunos, cursos e matrículas
- Endpoint customizado para marcar matrícula como paga
- Listar matrículas de um aluno específico
- Filtros básicos (por nome, status)

✅ **Relatórios:**
- Dashboard HTML com estatísticas
- Histórico do aluno com suas matrículas
- Relatório JSON: matrículas por curso
- Relatório JSON: total devido por aluno
- Relatório JSON: pagamentos pendentes

✅ **Docker:**
- docker-compose funcional com web + postgres
- Migrations automáticas
- Criação de superusuário automática
- Dados de exemplo carregados

### O que fiz mas não ficou perfeito

⚠️ **SQL Bruto:**
Consegui implementar consulta com JOIN e GROUP BY mas tive dificuldade com agregações múltiplas (SUM + COUNT + CASE WHEN juntos). O erro que recebi foi sobre "column must appear in GROUP BY clause". Entendo o conceito mas não consegui fazer funcionar. Implementei uma versão simplificada.

⚠️ **Otimização de queries:**
Sei que em alguns lugares estou fazendo N+1 queries (especialmente nos relatórios onde faço loop e chamo métodos dos objetos). Pesquisei sobre select_related() e prefetch_related() mas não consegui aplicar corretamente no tempo disponível.

⚠️ **Validações:**
As validações de CPF e email são básicas (só verificam formato e tamanho). Não implementei a validação completa do CPF com os dígitos verificadores. Sei que existe o algoritmo mas focando no prazo priorizei outras coisas.

⚠️ **Frontend:**
O CSS é bem básico. Não sou muito bom com design então deixei funcional mas simples. Em um projeto real trabalharia com alguém de front ou usaria um framework de componentes.

### O que não implementei

❌ **Testes automatizados:**
Não implementei testes unitários ou de integração. Tenho experiência com testes funcionais manuais (no trabalho faço isso durante implantações) mas não com testes automatizados. Vi pytest na faculdade mas não consegui aplicar aqui.

❌ **Funcionalidades extras:**
- Paginação nas listagens grandes
- Edição inline no admin
- Exportar relatórios em PDF/Excel
- Sistema de notificações
- Logs de auditoria

## Estrutura do projeto

```
academia-dev/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── manage.py
├── meu_database.sql
├── academia/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── core/
    ├── models.py
    ├── views.py
    ├── serializers.py
    ├── admin.py
    ├── urls.py
    └── templates/
```

## Tecnologias usadas

- Python 3.11
- Django 5.0
- Django REST Framework 3.14
- PostgreSQL 15
- Docker & Docker Compose

## Dificuldades que tive

### 1. SQL complexo
Tentei fazer uma query com múltiplas agregações mas travei. Pesquisei no Stack Overflow e na documentação do PostgreSQL mas não consegui resolver o erro do GROUP BY. Essa é uma área que preciso estudar mais.

### 2. Otimização
Percebi que algumas partes do código fazem muitas queries ao banco (N+1 problem). Sei que isso pode ser otimizado mas não consegui implementar a solução correta no prazo.

### 3. Frontend
Não sou designer, então o CSS ficou bem básico. Tentei deixar limpo e funcional mas reconheço que não é meu forte.

## O que aprendi fazendo esse desafio

- Como estruturar um projeto Django do zero
- Usar ViewSets do DRF pra APIs
- Configurar Docker com múltiplos serviços
- Relacionamentos entre models (ForeignKey)
- Executar SQL bruto com cursor() (mesmo que não tenha ficado perfeito)
- Priorizar funcionalidades quando tem prazo apertado

## Se tivesse mais tempo

- Implementaria testes automatizados (pelo menos pros models principais)
- Corrigiria a query SQL complexa
- Otimizaria as queries que estão causando N+1 problem
- Melhoraria o frontend (talvez usando Bootstrap de verdade)
- Adicionaria paginação
- Implementaria validação completa de CPF

## Observações

Esse foi meu primeiro projeto Django "completo" fora da faculdade. Tentei fazer o máximo possível com o conhecimento que tenho. Sei que tem coisas que podem melhorar e estou ansioso pra aprender mais.

Qualquer dúvida sobre as decisões que tomei ou como funciona alguma parte, é só perguntar!

---

**Contato:**  
Email: kaio.pinheiro.065@outlook.com  
LinkedIn: linkedin.com/in/kaio-cesar-de-sousa-pinheiro
