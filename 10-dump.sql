-- MySQL dump 10.13  Distrib 5.7.8-rc, for Linux (x86_64)
--
-- Host: localhost    Database: arsual_data_base
-- ------------------------------------------------------
-- Server version	5.7.8-rc

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Drop database
DROP DATABASE IF EXISTS arsual_data_base;

-- Create database + user if doesn't exist
CREATE DATABASE IF NOT EXISTS arsual_data_base;
CREATE USER IF NOT EXISTS 'arsual'@'localhost';
SET PASSWORD FOR 'arsual'@'localhost' = 'root';
GRANT ALL ON arsual_data_base.* TO 'arsual'@'localhost';
GRANT SELECT ON performance_schema.* TO 'arsual'@'localhost';
FLUSH PRIVILEGES;

USE arsual_data_base;

--
-- Table structure for table `artts`
--

DROP TABLE IF EXISTS `artts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `artts` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artts`
--

LOCK TABLES `artts` WRITE;
/*!40000 ALTER TABLE `artts` DISABLE KEYS */;
INSERT INTO `artts` VALUES ('821a55f4-7d82-47d9-b54c-a76916479551','2017-03-25 19:44:42','2017-03-25 19:44:42','Wifi'),('821a55f4-7d82-47d9-b54c-a76916479552','2017-03-25 19:44:42','2017-03-25 19:44:42','Pets friendly'),('821a55f4-7d82-47d9-b54c-a76916479553','2017-03-25 19:44:42','2017-03-25 19:44:42','Elevator in building'),('821a55f4-7d82-47d9-b54c-a76916479554','2017-03-25 19:44:42','2017-03-25 19:44:42','Doorman'),('821a55f4-7d82-47d9-b54c-a76916479555','2017-03-25 19:44:42','2017-03-25 19:44:42','Cable TV'),('821a55f4-7d82-47d9-b54c-a76916479556','2017-03-25 19:44:42','2017-03-25 19:44:42','Dryer'),('821a55f4-7d82-47d9-b54c-a76916479557','2017-03-25 19:44:42','2017-03-25 19:44:42','Hair dryer'),('821a55f4-7d82-47d9-b54c-a76916479558','2017-03-25 19:44:42','2017-03-25 19:44:42','Iron'),('821a55f4-7d82-47d9-b54c-a76916479559','2017-03-25 19:44:42','2017-03-25 19:44:42','Washer'),('821a55f4-7d82-47d9-b54c-a76916479560','2017-03-25 19:44:42','2017-03-25 19:44:42','Laundry room'),('821a55f4-7d82-47d9-b54c-a76916479561','2017-03-25 19:44:42','2017-03-25 19:44:42','Air conditioning'),('821a55f4-7d82-47d9-b54c-a76916479562','2017-03-25 19:44:42','2017-03-25 19:44:42','Hot tub'),('821a55f4-7d82-47d9-b54c-a76916479563','2017-03-25 19:44:42','2017-03-25 19:44:42','Smoking allowed');
/*!40000 ALTER TABLE `artts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scores`
--

DROP TABLE IF EXISTS `scores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scores` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scores`
--

LOCK TABLES `scores` WRITE;
/*!40000 ALTER TABLE `scores` DISABLE KEYS */;
INSERT INTO `scores` VALUES ('421a55f4-7d82-47d9-b54c-a76916479545','2017-03-25 19:44:42','2017-03-25 19:44:42','Alabama'),('421a55f4-7d82-47d9-b54c-a76916479546','2017-03-25 19:44:42','2017-03-25 19:44:42','Arizona'),('421a55f4-7d82-47d9-b54c-a76916479547','2017-03-25 19:44:42','2017-03-25 19:44:42','California'),('421a55f4-7d82-47d9-b54c-a76916479548','2017-03-25 19:44:42','2017-03-25 19:44:42','Colorado'),('421a55f4-7d82-47d9-b54c-a76916479549','2017-03-25 19:44:42','2017-03-25 19:44:42','Florida'),('421a55f4-7d82-47d9-b54c-a76916479550','2017-03-25 19:44:42','2017-03-25 19:44:42','Georgia'),('421a55f4-7d82-47d9-b54c-a76916479551','2017-03-25 19:44:42','2017-03-25 19:44:42','Hawaii'),('421a55f4-7d82-47d9-b54c-a76916479552','2017-03-25 19:44:42','2017-03-25 19:44:42','Illinois'),('421a55f4-7d82-47d9-b54c-a76916479553','2017-03-25 19:44:42','2017-03-25 19:44:42','Indiana'),('421a55f4-7d82-47d9-b54c-a76916479554','2017-03-25 19:44:42','2017-03-25 19:44:42','Louisiana'),('421a55f4-7d82-47d9-b54c-a76916479555','2017-03-25 19:44:42','2017-03-25 19:44:42','Minnesota'),('421a55f4-7d82-47d9-b54c-a76916479556','2017-03-25 19:44:42','2017-03-25 19:44:42','Mississippi'),('421a55f4-7d82-47d9-b54c-a76916479557','2017-03-25 19:44:42','2017-03-25 19:44:42','Oregon');
/*!40000 ALTER TABLE `scores` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-03-25 19:44:44
