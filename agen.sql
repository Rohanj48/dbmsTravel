-- MySQL dump 10.13  Distrib 8.0.35, for Win64 (x86_64)
--
-- Host: localhost    Database: agency
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `bid` int NOT NULL,
  `user_id` int DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `start` varchar(20) DEFAULT NULL,
  `dest` varchar(20) DEFAULT NULL,
  `nos` int DEFAULT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bus`
--

DROP TABLE IF EXISTS `bus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bus` (
  `bno` int NOT NULL,
  `bname` varchar(20) DEFAULT NULL,
  `start` varchar(20) DEFAULT NULL,
  `dest` varchar(20) DEFAULT NULL,
  `nosa` int DEFAULT NULL,
  PRIMARY KEY (`bno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bus`
--

LOCK TABLES `bus` WRITE;
/*!40000 ALTER TABLE `bus` DISABLE KEYS */;
INSERT INTO `bus` VALUES (2365,'orange','kozhikode','palakkad',45),(4578,'raj travels','thrissur','kollam',26),(5609,'sharma express','bangalore','goa',46),(9534,'ksrtc','kollam','kannur',15),(9845,'green travels','tvm','thrissur',23);
/*!40000 ALTER TABLE `bus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cust`
--

DROP TABLE IF EXISTS `cust`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cust` (
  `user_id` int NOT NULL,
  `pass` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cust`
--

LOCK TABLES `cust` WRITE;
/*!40000 ALTER TABLE `cust` DISABLE KEYS */;
INSERT INTO `cust` VALUES (123,'abc','amit'),(345,'lmn','ross'),(456,'pqr','dave'),(567,'def','robert'),(789,'xyz','john');
/*!40000 ALTER TABLE `cust` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight` (
  `fno` int NOT NULL,
  `fname` varchar(20) DEFAULT NULL,
  `start` varchar(20) DEFAULT NULL,
  `dest` varchar(20) DEFAULT NULL,
  `nosa` int DEFAULT NULL,
  PRIMARY KEY (`fno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight`
--

LOCK TABLES `flight` WRITE;
/*!40000 ALTER TABLE `flight` DISABLE KEYS */;
INSERT INTO `flight` VALUES (123,'jet airways','chennai','kolkata',32),(1245,'emirates','dubai','kochi',38),(3467,'silk air','mumbai','delhi',56),(6789,'air india','kochi','mumbai',34),(7890,'indigo','delhi','bangalore',25);
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `train`
--

DROP TABLE IF EXISTS `train`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `train` (
  `tno` int NOT NULL,
  `tname` varchar(30) DEFAULT NULL,
  `start` varchar(30) DEFAULT NULL,
  `dest` varchar(30) DEFAULT NULL,
  `nosa` int DEFAULT NULL,
  PRIMARY KEY (`tno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `train`
--

LOCK TABLES `train` WRITE;
/*!40000 ALTER TABLE `train` DISABLE KEYS */;
INSERT INTO `train` VALUES (1234,'pune express','tvm','pune',20),(2345,'intercity','kozhikode','kochi',14),(3456,'vande bharat','kollam','tvm',18),(4567,'rajdhani','pune','kochi',25),(5678,'orient','palakkad','kollam',23);
/*!40000 ALTER TABLE `train` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-19 12:08:42

str_to_date('21-12-2023','%d-%m-%Y')
INSERT INTO `bus` VALUES (2365,'orange','kozhikode','palakkad',45,str_to_date('21-12-2023','%d-%m-%Y')),(4578,'raj travels','thrissur','kollam',26,str_to_date('21-12-2023','%d-%m-%Y')),(5609,'sharma express','bangalore','goa',46,str_to_date('21-12-2023','%d-%m-%Y')),(9534,'ksrtc','kollam','kannur',15,str_to_date('21-12-2023','%d-%m-%Y')),(9845,'green travels','tvm','thrissur',23,str_to_date('21-12-2023','%d-%m-%Y'));

str_to_date('21-12-2023','%d-%m-%Y')
INSERT INTO `train` VALUES (1234,'pune express','tvm','pune',20,str_to_date('21-12-2023','%d-%m-%Y')),(2345,'intercity','kozhikode','kochi',14,str_to_date('21-12-2023','%d-%m-%Y')),(3456,'vande bharat','kollam','tvm',18,str_to_date('21-12-2023','%d-%m-%Y')),(4567,'rajdhani','pune','kochi',25,str_to_date('21-12-2023','%d-%m-%Y')),(5678,'orient','palakkad','kollam',23,str_to_date('21-12-2023','%d-%m-%Y'));

INSERT INTO `flight` VALUES (123,'jet airways','chennai','kolkata',32,str_to_date('21-12-2023','%d-%m-%Y')),(1245,'emirates','dubai','kochi',38,str_to_date('21-12-2023','%d-%m-%Y')),(3467,'silk air','mumbai','delhi',56,str_to_date('21-12-2023','%d-%m-%Y')),(6789,'air india','kochi','mumbai',34,str_to_date('21-12-2023','%d-%m-%Y')),(7890,'indigo','delhi','bangalore',25,str_to_date('21-12-2023','%d-%m-%Y'));