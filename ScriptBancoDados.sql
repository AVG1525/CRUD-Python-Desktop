CREATE DATABASE py;
USE py;

/*TABELAS*/
CREATE TABLE Users(
users_id INT PRIMARY KEY AUTO_INCREMENT,
users_nome VARCHAR(100) NOT NULL,
users_idade INT(4) NOT NULL,
users_email VARCHAR(50) NOT NULL,
users_senha VARCHAR(33) NOT NULL,
);

/*INSERTS*/
INSERT INTO usuarios VALUES
(DEFAULT, 'Aron', 18, 'aron@aron.com', '9835260c7cabe24ce31b19d327596951');

