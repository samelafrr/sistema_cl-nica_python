-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           9.6.0 - MySQL Community Server - GPL
-- OS do Servidor:               Win64
-- HeidiSQL Versão:              12.16.0.7229
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Copiando estrutura do banco de dados para db_sys_clinic
DROP DATABASE IF EXISTS `db_sys_clinic`;
CREATE DATABASE IF NOT EXISTS `db_sys_clinic` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db_sys_clinic`;

-- Copiando estrutura para tabela db_sys_clinic.tb_agendamentos
DROP TABLE IF EXISTS `tb_agendamentos`;
CREATE TABLE IF NOT EXISTS `tb_agendamentos` (
  `id_agendamento` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int NOT NULL,
  `id_medico` int NOT NULL,
  `data_agendamento` date NOT NULL,
  `hora_agendamento` time NOT NULL,
  `observacao` varchar(255) DEFAULT '',
  `status_agendamento` varchar(20) NOT NULL DEFAULT 'Agendado',
  PRIMARY KEY (`id_agendamento`),
  KEY `FK_tb_agendamentos_tb_clientes` (`id_cliente`),
  KEY `FK_tb_agendamentos_id_medicos` (`id_medico`),
  CONSTRAINT `FK_tb_agendamentos_id_medicos` FOREIGN KEY (`id_medico`) REFERENCES `tb_medicos` (`id_medico`),
  CONSTRAINT `FK_tb_agendamentos_tb_clientes` FOREIGN KEY (`id_cliente`) REFERENCES `tb_clientes` (`id_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Copiando dados para a tabela db_sys_clinic.tb_agendamentos: ~2 rows (aproximadamente)
INSERT INTO `tb_agendamentos` (`id_agendamento`, `id_cliente`, `id_medico`, `data_agendamento`, `hora_agendamento`, `observacao`, `status_agendamento`) VALUES
	(2, 2, 2, '2026-04-15', '13:00:00', '', ''),
	(3, 3, 3, '2026-04-19', '13:00:00', '', 'Agendado');

-- Copiando estrutura para tabela db_sys_clinic.tb_clientes
DROP TABLE IF EXISTS `tb_clientes`;
CREATE TABLE IF NOT EXISTS `tb_clientes` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nome_cliente` varchar(150) NOT NULL,
  `telefone` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `inativo` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_cliente`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Copiando dados para a tabela db_sys_clinic.tb_clientes: ~5 rows (aproximadamente)
INSERT INTO `tb_clientes` (`id_cliente`, `nome_cliente`, `telefone`, `email`, `inativo`) VALUES
	(2, 'Lucas Cardoso Costa', '83986828019', 'lucascardosocst@gmail.com', 1),
	(3, 'Samela Feitosa', '83 986808989', 'samela.ferreira@gmail.com', 0),
	(4, 'Maraine Lima', '83 9 7654321', 'mari.lima@gmail.com', 0),
	(5, 'Luana Moraes', '83 9 878585291', 'launa.moraes@gmail.com', 0),
	(6, 'Nayara Silva', '83980909809', 'nayara.silva@gmail.com', 0);

-- Copiando estrutura para tabela db_sys_clinic.tb_medicos
DROP TABLE IF EXISTS `tb_medicos`;
CREATE TABLE IF NOT EXISTS `tb_medicos` (
  `id_medico` int NOT NULL AUTO_INCREMENT,
  `nome_medico` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `telefone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `crm` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `especialidade` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id_medico`),
  UNIQUE KEY `nome_medico` (`nome_medico`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Copiando dados para a tabela db_sys_clinic.tb_medicos: ~5 rows (aproximadamente)
INSERT INTO `tb_medicos` (`id_medico`, `nome_medico`, `telefone`, `crm`, `especialidade`) VALUES
	(2, 'Dra. Annelise', '83987855291', '45326', 'Dermatologista'),
	(3, 'Dr. Stefano', '83 981845678', '3247', 'Cardiologista'),
	(4, 'Dra. Bianca Gadelha', '83 988000088', '789009', 'Neurologista'),
	(5, 'Dr. Matheus Costa', '83 912345678', '12345', 'Gastro'),
	(6, 'Dra. Flaviana Lopes', '83 917189090', '56789', 'Ortopedista');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
