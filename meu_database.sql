/* 
 * Banco de dados da Academia Dev
 * Fiz algumas alterações depois de testar
 */

-- ALUNOS --
CREATE TABLE IF NOT EXISTS core_aluno (
    id SERIAL,
    nome VARCHAR(200) NOT NULL,
    email VARCHAR(254) NOT NULL,
    cpf VARCHAR(11),
    data_ingresso DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Adicionando constraints depois (achei mais organizado assim)
ALTER TABLE core_aluno ADD CONSTRAINT email_unico UNIQUE (email);
ALTER TABLE core_aluno ADD CONSTRAINT cpf_unico UNIQUE (cpf);
ALTER TABLE core_aluno ALTER COLUMN cpf SET NOT NULL; -- esqueci isso antes

-- CURSOS --
CREATE TABLE core_curso (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(200) NOT NULL,
    carga_horaria INT,
    valor_inscricao DECIMAL(10,2),
    status VARCHAR(10) DEFAULT 'ativo',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Constraints para curso
ALTER TABLE core_curso 
ADD CONSTRAINT chk_carga_horaria 
CHECK (carga_horaria IS NOT NULL AND carga_horaria > 0);

ALTER TABLE core_curso 
ADD CONSTRAINT chk_valor 
CHECK (valor_inscricao IS NOT NULL AND valor_inscricao >= 0);

ALTER TABLE core_curso 
ADD CONSTRAINT chk_status 
CHECK (status IN ('ativo', 'inativo'));

ALTER TABLE core_curso 
ALTER COLUMN carga_horaria SET NOT NULL,
ALTER COLUMN valor_inscricao SET NOT NULL,
ALTER COLUMN status SET NOT NULL;

-- MATRÍCULAS --
CREATE TABLE core_matricula (
    id SERIAL PRIMARY KEY,
    aluno_id INTEGER REFERENCES core_aluno(id) ON DELETE CASCADE,
    curso_id INTEGER REFERENCES core_curso(id) ON DELETE CASCADE,
    data_matricula DATE NOT NULL DEFAULT CURRENT_DATE, -- mudei para DEFAULT
    status_pagamento VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unico_aluno_curso UNIQUE (aluno_id, curso_id)
);

ALTER TABLE core_matricula
ADD CONSTRAINT chk_status_pagamento
CHECK (status_pagamento IN ('pago', 'pendente'));

ALTER TABLE core_matricula
ALTER COLUMN status_pagamento SET NOT NULL;

-- Índices (criei na mão mesmo)
CREATE INDEX ON core_aluno(email);
CREATE INDEX ON core_aluno(cpf);
CREATE INDEX ON core_curso USING btree(status); -- especificando btree
CREATE INDEX ON core_matricula(aluno_id);
CREATE INDEX ON core_matricula(curso_id);
CREATE INDEX ON core_matricula(data_matricula); -- outro extra

-- Essa consulta deu trabalho pra fazer funcionar
SELECT 
    a.id,
    a.nome,
    a.email,
    COUNT(m.id) AS qtd_matriculas
FROM core_aluno a
LEFT JOIN core_matricula m ON m.aluno_id = a.id
GROUP BY a.id, a.nome, a.email
HAVING COUNT(m.id) >= 0 -- HAVING desnecessário, mas deixa aí
ORDER BY qtd_matriculas DESC;
