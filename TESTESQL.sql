CREATE DATABASE TESTESSQL
USE TESTESSQL

CREATE TABLE usuarios (
    id INT IDENTITY(1,1) PRIMARY KEY, -- Identificador único do usuário
    nome VARCHAR(100) NOT NULL, -- Nome completo
    email VARCHAR(255) UNIQUE NOT NULL, -- Email único para login
    telefone VARCHAR(20) NULL, -- Número de telefone (opcional)
    data_nascimento DATE NULL, -- Data de nascimento (opcional)
    cpf CHAR(11) UNIQUE NULL, -- CPF do usuário (opcional, Brasil)
    endereco TEXT NULL, -- Endereço completo
    cidade VARCHAR(100) NULL, -- Cidade do usuário
    estado VARCHAR(50) NULL, -- Estado/Região
    pais VARCHAR(50) NULL DEFAULT 'Brasil', -- País (padrão Brasil)
    data_cadastro DATETIME DEFAULT GETDATE(), -- Data do cadastro
    ultimo_login DATETIME NULL, -- Último login do usuário
);

INSERT INTO usuarios (nome, email, telefone, data_nascimento, cpf, endereco, cidade, estado, pais, data_cadastro, ultimo_login) VALUES
('João Silva', 'joao.silva@email.com', '11999999999', '1990-05-15', '12345678901', 'Rua A, 100', 'São Paulo', 'SP', 'Brasil', GETDATE(), NULL),
('Maria Oliveira', 'maria.oliveira@email.com', '21988888888', '1985-10-20', '23456789012', 'Av. B, 200', 'Rio de Janeiro', 'RJ', 'Brasil', GETDATE(), NULL),
('Carlos Souza', 'carlos.souza@email.com', '31977777777', '1992-03-10', '34567890123', 'Rua C, 300', 'Belo Horizonte', 'MG', 'Brasil', GETDATE(), NULL),
('Ana Santos', 'ana.santos@email.com', '41966666666', '1988-07-25', '45678901234', 'Av. D, 400', 'Curitiba', 'PR', 'Brasil', GETDATE(), NULL),
('Lucas Mendes', 'lucas.mendes@email.com', '51955555555', '1995-12-05', '56789012345', 'Rua E, 500', 'Porto Alegre', 'RS', 'Brasil', GETDATE(), NULL),
('Fernanda Lima', 'fernanda.lima@email.com', '61944444444', '1993-08-30', '67890123456', 'Av. F, 600', 'Brasília', 'DF', 'Brasil', GETDATE(), NULL),
('Ricardo Alves', 'ricardo.alves@email.com', '71933333333', '1980-02-14', '78901234567', 'Rua G, 700', 'Salvador', 'BA', 'Brasil', GETDATE(), NULL),
('Juliana Rocha', 'juliana.rocha@email.com', '81922222222', '1991-06-18', '89012345678', 'Av. H, 800', 'Recife', 'PE', 'Brasil', GETDATE(), NULL),
('Pedro Martins', 'pedro.martins@email.com', '91911111111', '1987-09-09', '90123456789', 'Rua I, 900', 'Fortaleza', 'CE', 'Brasil', GETDATE(), NULL),
('Camila Ferreira', 'camila.ferreira@email.com', '11900000000', '1999-04-22', '01234567890', 'Av. J, 1000', 'Manaus', 'AM', 'Brasil', GETDATE(), NULL);
GO

INSERT INTO usuarios (nome, email, telefone, data_nascimento, cpf, endereco, cidade, estado, pais, data_cadastro, ultimo_login) VALUES
('João Victor de Souza Fontes', 'souzafontesjoaovictor2@gmail.com', '14988169659', '2004-02-23', '12345078901', 'Rua A, 100', 'São Paulo', 'SP', 'Brasil', GETDATE(), NULL);

SELECT*FROM usuarios;