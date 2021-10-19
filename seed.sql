-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: company_db_simulation
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client` (
  `client_name` varchar(40) NOT NULL,
  `client_location` varchar(40) DEFAULT NULL,
  `dep_id` int DEFAULT NULL,
  PRIMARY KEY (`client_name`),
  KEY `dep_id` (`dep_id`),
  CONSTRAINT `client_ibfk_1` FOREIGN KEY (`dep_id`) REFERENCES `works_on` (`dep_id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES ('Company_1','California, USA',3),('Company_2','Alberta, Canada',4),('Company_3','Michigan, USA',3);
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `dep_id` int NOT NULL,
  `dep_name` varchar(40) NOT NULL,
  `location` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`dep_id`,`dep_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'Corporate','Sofia'),(2,'Sales','Sofia'),(3,'IT','Sofia'),(4,'IT','Plovdiv');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_main_info`
--

DROP TABLE IF EXISTS `employee_main_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_main_info` (
  `emp_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(40) DEFAULT NULL,
  `last_name` varchar(40) DEFAULT NULL,
  `birth_day` date DEFAULT NULL,
  `sex` varchar(1) DEFAULT NULL,
  `social_security_number` varchar(40) DEFAULT NULL,
  `salary` int DEFAULT NULL,
  `dep_id` int DEFAULT NULL,
  `project_id` int DEFAULT NULL,
  `location` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`emp_id`),
  KEY `dep_id` (`dep_id`),
  KEY `project_id` (`project_id`),
  CONSTRAINT `employee_main_info_ibfk_1` FOREIGN KEY (`dep_id`) REFERENCES `department` (`dep_id`) ON DELETE SET NULL,
  CONSTRAINT `employee_main_info_ibfk_2` FOREIGN KEY (`project_id`) REFERENCES `project` (`project_id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=1002 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_main_info`
--

LOCK TABLES `employee_main_info` WRITE;
/*!40000 ALTER TABLE `employee_main_info` DISABLE KEYS */;
INSERT INTO `employee_main_info` VALUES (1001,'John','Smith','1987-03-15','M','æp÷öÚ’üÒÁ\r É)ñ³',3000,3,501,'Sofia');
/*!40000 ALTER TABLE `employee_main_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login_info`
--

DROP TABLE IF EXISTS `login_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login_info` (
  `username` varchar(40) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login_info`
--

LOCK TABLES `login_info` WRITE;
/*!40000 ALTER TABLE `login_info` DISABLE KEYS */;
INSERT INTO `login_info` VALUES ('admin','961302f886378a116f44d987c3426fdc48d66a89855596c6a947b0b42e8e0505'),('johny','c7d263cad171d4d9d7ea90f7890ae688cc959825c950d5f85feee581d6fbf8a4');
/*!40000 ALTER TABLE `login_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project` (
  `project_id` int NOT NULL,
  `project_name` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`project_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (500,'Compute and Data Center'),(501,'Storage and Backup'),(502,'Network');
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `works_on`
--

DROP TABLE IF EXISTS `works_on`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `works_on` (
  `dep_id` int NOT NULL,
  `project_id` int NOT NULL,
  `client_name` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`dep_id`,`project_id`),
  KEY `project_id` (`project_id`),
  CONSTRAINT `works_on_ibfk_1` FOREIGN KEY (`dep_id`) REFERENCES `department` (`dep_id`) ON DELETE CASCADE,
  CONSTRAINT `works_on_ibfk_2` FOREIGN KEY (`project_id`) REFERENCES `project` (`project_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `works_on`
--

LOCK TABLES `works_on` WRITE;
/*!40000 ALTER TABLE `works_on` DISABLE KEYS */;
INSERT INTO `works_on` VALUES (3,500,'Company_3'),(3,501,'Company_1'),(4,502,'Company_2');
/*!40000 ALTER TABLE `works_on` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-19 17:04:57
