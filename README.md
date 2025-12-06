# 🎓 Sistema Academia Dev Python / Devs do RN

Sistema desenvolvido como parte do desafio técnico para vaga de estágio.

**Desenvolvedor:** Kaio Cesar De Sousa Pinheiro  
**Tempo de desenvolvimento:** ~18 horas  
**Data:** Dezembro 2025

---

## 📊 Status de Implementação

### ✅ Funcionalidades Completas (~75%)

#### Backend:
- ✅ Models com relacionamentos básicos
- ✅ CRUD de Alunos/Associados
- ✅ CRUD de Cursos/Anuidades
- ✅ Sistema de matrículas/pagamentos
- ✅ Admin do Django configurado
- ✅ API REST básica (GET, POST)
- ✅ Docker + PostgreSQL/MySQL funcionando

#### Frontend:
- ✅ Templates HTML funcionais
- ✅ Dashboard com estatísticas
- ✅ Formulários de cadastro
- ✅ CSS básico responsivo

### ⚠️ Parcialmente Implementadas (~15%)

#### SQL Bruto:
- ⚠️ Implementei consultas com JOIN básico
- ❌ **Não consegui:** Agregações múltiplas (SUM + COUNT + CASE WHEN)
- **Dificuldade:** Erro "column must appear in GROUP BY clause"
- **Aprendi:** Conceito de GROUP BY, mas preciso praticar mais sintaxe complexa

#### Validações:
- ⚠️ Validações de formato (email, CPF tamanho)
- ❌ **Não consegui:** Validação completa de CPF (dígitos verificadores)
- **Motivo:** Conheço o conceito mas não implementei o algoritmo

#### Otimização:
- ⚠️ Queries funcionam mas podem causar N+1 problem
- ❌ **Não consegui:** Otimizar com select_related()/prefetch_related()
- **Aprendi:** O problema existe, mas preciso estudar mais a solução

### ❌ Não Implementadas (~10%)

#### Testes Automatizados:
- **Status:** Não implementado
- **Motivo:** Focando no tempo, priorizei funcionalidades core
- **Experiência:** Faço testes funcionais manuais no trabalho atual
- **Próximo passo:** Estudar TestCase do Django e implementar

#### Funcionalidades Avançadas:
- Sistema de autenticação/permissões
- Relatórios em PDF
- Paginação de listagens
- Filtros avançados na API

---

## 🎯 Decisões Técnicas

### Por que Django/PHP Puro?
Escolhi [Django/PHP] porque tenho experiência prévia:
- Django: projetos na UFRN (disciplinas)
- PHP: freelas autônomos
- Python: mais confortável com sintaxe

### Por que PostgreSQL/MySQL?
- Experiência em projetos acadêmicos
- Docker compose facilita setup
- Conhecimento de SQL básico

### Por que Docker?
- Experiência profissional (Clínica Oitava Rosado - infraestrutura)
- Garante ambiente consistente
- Facilita avaliação do projeto

---

## 🤔 Dificuldades Encontradas

### 1. SQL Avançado
**Problema:** Agregações múltiplas com GROUP BY  
**Tentativa:** Pesquisei documentação PostgreSQL e Stack Overflow  
**Resultado:** Consegui JOIN básico mas não a versão completa  
**Aprendizado:** Entendi que preciso praticar mais SQL complexo

### 2. Otimização de Queries
**Problema:** N+1 queries nos relatórios  
**Tentativa:** Li sobre select_related() e prefetch_related()  
**Resultado:** Não consegui aplicar corretamente  
**Aprendizado:** Sei que o problema existe e onde estudar

### 3. Frontend
**Contexto:** Meu foco é backend  
**Resultado:** CSS básico mas funcional  
**Decisão:** Priorizei tempo no backend e APIs

---

## 📚 O Que Aprendi

### Conceitos Novos:
- Como estruturar projeto Django do zero
- Diferença entre ViewSets e APIView
- Prepared statements no PDO (PHP)
- Docker multi-container com healthcheck

### Conceitos Reforçados:
- Relacionamentos entre tabelas (ForeignKey)
- REST API patterns
- MVC architecture
- Git workflow

### Áreas para Aprofundar:
- [ ] SQL avançado (agregações, subqueries, window functions)
- [ ] Testes automatizados (pytest, unittest)
- [ ] Otimização de queries (ORM)
- [ ] Frontend moderno (React, Vue)

---

## 🔄 Se Tivesse Mais Tempo

### Curto Prazo (1 semana):
1. Implementar testes automatizados básicos
2. Corrigir SQL bruto com agregações
3. Adicionar paginação nas listagens
4. Melhorar validações

### Médio Prazo (1 mês):
1. Sistema de autenticação completo
2. Otimizar todas as queries
3. Frontend mais elaborado
4. Deploy em produção (Heroku/Railway)

---

## 💡 Feedback do Processo

Este desafio me fez:
- **Sair da zona de conforto:** SQL complexo e APIs REST
- **Priorizar funcionalidades:** Foco no que agrega mais valor
- **Documentar limitações:** Honestidade sobre o que não sei
- **Pensar em escalabilidade:** Mesmo sem implementar tudo

**Maior aprendizado:** Não preciso saber tudo, preciso saber onde aprender.

---

## 🚀 Como Rodar
```bash
docker-compose up --build
# Acesse: http://localhost:8000 (Django) ou :8080 (PHP)
# Admin: admin / admin123
```

---

## 📧 Contato

**Kaio Cesar De Sousa Pinheiro**  
Email: kaio.pinheiro.065@outlook.com  
LinkedIn: linkedin.com/in/kaio-cesar-de-sousa-pinheiro  
Telefone: +55 84 99183-0438

---

**Obrigado pela oportunidade de participar do processo!**
```
