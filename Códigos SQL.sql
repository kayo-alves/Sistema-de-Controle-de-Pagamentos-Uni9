
-- TABELA EMPRESA
CREATE TABLE empresa (
    id_emp INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(20) NOT NULL,
    cnpj char(18) not null unique,
    ramo_atuacao varchar(35) not null
    );

INSERT INTO empresa (id_emp, nome, cnpj, ramo_atuacao) VALUES (120, 'LedaLog', '12.345.678/0001-95', 'Logística');
INSERT INTO empresa (id_emp, nome, cnpj, ramo_atuacao) VALUES (130, 'MarKing', '98.765.432/0001-80', 'Marketing Digital e publicidade');
INSERT INTO empresa (id_emp, nome, cnpj, ramo_atuacao) VALUES (140, 'AdvDireito', '45.678.901/0001-37', 'Advocacia em geral');


------------------------------------

-- TABELA DEPARTAMENTO
CREATE TABLE departamento (
    id_depart INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO departamento (id_depart, nome) VALUES (10, 'Departamento Logístico');
INSERT INTO departamento (id_depart, nome) VALUES (default, 'Departamento de Tecnologia da Informação');
INSERT INTO departamento (id_depart, nome) VALUES (default, 'Departamento Jurídico');
INSERT INTO departamento (id_depart, nome) VALUES (default, 'Departamento de Marketing');

----------------------------------------
-- TABELA CARGO 
CREATE TABLE cargo (
    id_cargo INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    salario DECIMAL(7,2) NOT NULL
);

INSERT INTO cargo (id_cargo, nome, salario) VALUES (1, 'Operador Logístico', 3500);
INSERT INTO cargo (id_cargo, nome, salario) VALUES (default, 'Programador', 9800);
INSERT INTO cargo (id_cargo, nome, salario) VALUES (default, 'Defensor Público', 8300);
INSERT INTO cargo (id_cargo, nome, salario) VALUES (default, 'Gerente de Marketing', 7500);


---------------------------------------

-- TABELA FUNCIONÁRIO
CREATE TABLE funcionario (
    id_funcionario INT NOT NULL  AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    cpf CHAR(11) NOT NULL UNIQUE,
    endereco VARCHAR(100) NOT NULL,
    dt_contratacao DATE NOT NULL,
    id_cargo INT,
    id_emp INT,
    CONSTRAINT fk_id_cargo FOREIGN KEY (id_cargo) REFERENCES cargo(id_cargo),
    CONSTRAINT fk_id_emp FOREIGN KEY (id_emp) REFERENCES empresa(id_emp)
);
INSERT INTO funcionario (id_funcionario, nome, cpf, endereco, dt_contratacao, id_cargo, id_emp) 
VALUES (20, 'Marcos Alexandre Batista', '99887766444', 'Santana, SP', '2021-02-26', 1, 120);

INSERT INTO funcionario (id_funcionario, nome, cpf, endereco, dt_contratacao, id_cargo, id_emp) 
VALUES (default, 'Bianca Oliveira R', '11223344555', 'Carapicuíba, SP', '2018-05-15', 2, 120);

INSERT INTO funcionario (id_funcionario, nome, cpf, endereco, dt_contratacao, id_cargo, id_emp) 
VALUES (default, 'Edilson dos Santos', '12345678999', 'Mariana, SP', '2020-10-10', 3, 120);

INSERT INTO funcionario (id_funcionario, nome, cpf, endereco, dt_contratacao, id_cargo, id_emp) 
VALUES (default, 'Elias Miguel Chagas', '68081781537', 'Tatuape, SP', '2023-10-10', 2, 120);

INSERT INTO funcionario (id_funcionario, nome, cpf, endereco, dt_contratacao, id_cargo, id_emp) 
VALUES (default, 'Arthur Figueiredo', '55395379383', 'Itapevi, SP', '2024-10-11', 2, 120);

INSERT INTO funcionario (id_funcionario, nome, cpf, endereco, dt_contratacao, id_cargo, id_emp) 
VALUES (default, 'José Kayo', '12465479881', 'Rua dos Paraíbas, SP', '2024-05-11', 2, 120);

INSERT INTO funcionario (id_funcionario, nome, cpf, endereco, dt_contratacao, id_cargo, id_emp) 
VALUES (default, 'Diogo Miranda', '12345698778', 'Rua de Osasco, SP', '2024-03-02', 1, 120);

INSERT INTO funcionario (id_funcionario, nome, cpf, endereco, dt_contratacao, id_cargo, id_emp) 
VALUES (default, 'Miguel Anjinho', '32165978998', 'Rua da Brasilândia, SP', '2023-06-18', 3, 120);

INSERT INTO funcionario (id_funcionario, nome, cpf, endereco, dt_contratacao, id_cargo, id_emp) 
VALUES (default, 'Emily Araújo', '92175685485', 'Rua da Brasilândia, SP', '2024-10-27', 4, 120);

-----------------------------------------------

-- TABELA FUNCIONÁRIO DEPARTAMENTO
CREATE TABLE funcionario_departamento (
    id_funcionario INT,
    id_depart INT,
    data_locacao DATE NOT NULL,
    data_saida DATE,
    PRIMARY KEY (id_funcionario, id_depart),
    CONSTRAINT fk_id_funcionario FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario),
    CONSTRAINT fk_id_depart FOREIGN KEY (id_depart) REFERENCES departamento(id_depart)
);
INSERT INTO funcionario_departamento (id_funcionario, id_depart, data_locacao, data_saida) 
VALUES(20, 10, '2024-03-03', NULL );

INSERT INTO funcionario_departamento (id_funcionario, id_depart, data_locacao, data_saida) 
VALUES(21, 11, '2018-05-16', NULL);

INSERT INTO funcionario_departamento (id_funcionario, id_depart, data_locacao, data_saida) 
VALUES(22, 11, '2018-10-11', NULL );


INSERT INTO funcionario_departamento (id_funcionario, id_depart, data_locacao, data_saida) 
VALUES(23, 11, '2023-10-11', NULL );

INSERT INTO funcionario_departamento (id_funcionario, id_depart, data_locacao, data_saida) 
VALUES(24, 11, '2024-10-12', NULL );

INSERT INTO funcionario_departamento (id_funcionario, id_depart, data_locacao, data_saida) 
VALUES(25, 11, '2024-05-12', NULL );

INSERT INTO funcionario_departamento (id_funcionario, id_depart, data_locacao, data_saida) 
VALUES(26, 10, '2024-03-03', NULL );

INSERT INTO funcionario_departamento (id_funcionario, id_depart, data_locacao, data_saida) 
VALUES(27, 12, '2023-06-19', NULL );

INSERT INTO funcionario_departamento (id_funcionario, id_depart, data_locacao, data_saida) 
VALUES(28, 13, '2024-10-28', NULL );

---------------------------------------

-- TABELA PAGAMENTO
CREATE TABLE pagamento (
    id_pag INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    hora_extra time,
    desconto decimal(7,2),
    data_pag DATE NOT NULL,
    pag_total DECIMAL(7,2) NOT NULL,
    id_funcionario INT,
    CONSTRAINT fk_id_funcionario_pag FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario)
);
 INSERT INTO pagamento (id_pag, id_funcionario, hora_extra, desconto,  data_pag, pag_total) 
VALUES (1, 20, null, null, '2024-04-03', 3500.00); 

 INSERT INTO pagamento (id_pag, id_funcionario, hora_extra, desconto,  data_pag, pag_total) 
VALUE (default, 21, null, null, '2018-06-16', 9800.00); 

 INSERT INTO pagamento (id_pag, id_funcionario, hora_extra, desconto, data_pag, pag_total) 
VALUE (default, 22, null, null, '2018-11-11', 8300.00);

 INSERT INTO pagamento (id_pag, id_funcionario, hora_extra, desconto,  data_pag, pag_total) 
VALUE (default, 23, null, null, '2023-11-11', 9800.00);




