-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: kaimosi_inventory_management_system_db
-- ------------------------------------------------------
-- Server version	8.0.42

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
-- Table structure for table `alerts`
--

DROP TABLE IF EXISTS `alerts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alerts` (
  `AssetID` int DEFAULT NULL,
  `AlertDate` date DEFAULT NULL,
  `AlertMessage` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alerts`
--

LOCK TABLES `alerts` WRITE;
/*!40000 ALTER TABLE `alerts` DISABLE KEYS */;
INSERT INTO `alerts` VALUES (3,'2025-05-20','Low stock for Hydrochloric Acid'),(7,'2025-05-21','Low stock for Disposable Face Masks');
/*!40000 ALTER TABLE `alerts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asset`
--

DROP TABLE IF EXISTS `asset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asset` (
  `AssetID` int NOT NULL AUTO_INCREMENT,
  `AssetCode` varchar(20) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Description` varchar(200) DEFAULT NULL,
  `CategoryID` int DEFAULT NULL,
  `DepartmentID` int NOT NULL,
  `LocationID` int NOT NULL,
  `PurchaseDate` date DEFAULT NULL,
  `Status` enum('Available','Assigned','Retired') NOT NULL,
  PRIMARY KEY (`AssetID`),
  KEY `IDX_ASSET_ASSETCODE` (`AssetCode`),
  KEY `fk_category` (`CategoryID`),
  KEY `fk_department` (`DepartmentID`),
  KEY `fk_location` (`LocationID`),
  CONSTRAINT `asset_ibfk_1` FOREIGN KEY (`CategoryID`) REFERENCES `category` (`CategoryID`) ON DELETE RESTRICT,
  CONSTRAINT `asset_ibfk_2` FOREIGN KEY (`DepartmentID`) REFERENCES `department` (`DepartmentID`) ON DELETE RESTRICT,
  CONSTRAINT `asset_ibfk_3` FOREIGN KEY (`LocationID`) REFERENCES `location` (`LocationID`) ON DELETE RESTRICT,
  CONSTRAINT `fk_category` FOREIGN KEY (`CategoryID`) REFERENCES `category` (`CategoryID`),
  CONSTRAINT `fk_department` FOREIGN KEY (`DepartmentID`) REFERENCES `department` (`DepartmentID`),
  CONSTRAINT `fk_location` FOREIGN KEY (`LocationID`) REFERENCES `location` (`LocationID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asset`
--

LOCK TABLES `asset` WRITE;
/*!40000 ALTER TABLE `asset` DISABLE KEYS */;
INSERT INTO `asset` VALUES (1,'L1','HP 840G3','14 INCH',1,1,1,'2025-05-24','Available'),(2,'L2','MacBook Pro','14-inch, M1 chip',1,1,1,'2024-06-10','Assigned'),(3,'REAGENT-001','Hydrochloric Acid','500ml, 37% concentration',1,1,1,'2024-03-10','Available'),(4,'BOOK-001','Data Structures Textbook','Introduction to Algorithms, 3rd Ed.',1,1,1,'2023-09-01','Assigned'),(5,'DESK-001','Wooden Desk','Standard classroom desk',1,1,1,'2022-06-20','Available'),(6,'PEN-001','Ballpoint Pen Pack','Pack of 50 pens',1,1,1,'2025-01-05','Available'),(7,'PPE-001','Disposable Face Masks','Box of 100 masks',1,1,1,'2024-11-12','Available'),(8,'BALL-001','Basketball','Standard size 7 basketball',1,1,1,'2023-08-15','Assigned'),(9,'PROJ-001','Epson Projector','4K projector for presentations',1,1,1,'2024-02-28','Available'),(10,'CHAIR-001','Ergonomic Chair','Adjustable office chair',1,1,1,'2023-12-01','Available'),(11,'LAPTOP-001','Dell XPS 13','13-inch laptop, 16GB RAM',1,1,1,'2024-01-15','Available'),(12,'LAPTOP-002','MacBook Pro','14-inch, M1 chip',1,1,3,'2024-06-10','Assigned'),(13,'REAGENT-001','Hydrochloric Acid','500ml, 37% concentration',2,2,1,'2024-03-10','Available'),(14,'DESK-001','Wooden Desk','Standard classroom desk',4,4,3,'2022-06-20','Available'),(15,'BOOK-001','Data Structures Textbook','Introduction to Algorithms, 3rd Ed.',3,3,2,'2023-09-01','Assigned'),(16,'PEN-001','Ballpoint Pen Pack','Pack of 50 pens',5,4,6,'2025-01-05','Available'),(17,'PPE-001','Disposable Face Masks','Box of 100 masks',6,6,5,'2024-11-12','Available'),(18,'BALL-001','Basketball','Standard size 7 basketball',7,4,4,'2023-08-15','Assigned'),(19,'PROJ-001','Epson Projector','4K projector for presentations',8,1,3,'2024-02-28','Available'),(20,'CHAIR-001','Ergonomic Chair','Adjustable office chair',4,4,6,'2023-12-01','Available');
/*!40000 ALTER TABLE `asset` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `CategoryID` int NOT NULL AUTO_INCREMENT,
  `CategoryName` varchar(50) NOT NULL,
  PRIMARY KEY (`CategoryID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Ict lab equipment'),(2,'lab supplies'),(3,'library materials'),(4,'furniture'),(5,'office supplies'),(6,'medical supplies'),(7,'sports equipment'),(8,'AV equipment');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `DepartmentID` int NOT NULL AUTO_INCREMENT,
  `DepartmentName` varchar(50) NOT NULL,
  PRIMARY KEY (`DepartmentID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'library services'),(2,'SCIT'),(3,'Nursing'),(4,'Entertainment'),(6,'Health');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `location` (
  `LocationID` int NOT NULL AUTO_INCREMENT,
  `LocationName` varchar(50) NOT NULL,
  PRIMARY KEY (`LocationID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (1,'scit lab 1'),(2,'scit lab 2'),(3,'library'),(4,'lecture halls'),(5,'Health center'),(6,'Storage room');
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stocklevel`
--

DROP TABLE IF EXISTS `stocklevel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stocklevel` (
  `StockID` int NOT NULL AUTO_INCREMENT,
  `AssetID` int DEFAULT NULL,
  `LocationID` int DEFAULT NULL,
  `Quantity` int NOT NULL,
  `MinThreshold` int NOT NULL,
  PRIMARY KEY (`StockID`),
  KEY `AssetID` (`AssetID`),
  KEY `LocationID` (`LocationID`),
  CONSTRAINT `stocklevel_ibfk_1` FOREIGN KEY (`AssetID`) REFERENCES `asset` (`AssetID`) ON DELETE CASCADE,
  CONSTRAINT `stocklevel_ibfk_2` FOREIGN KEY (`LocationID`) REFERENCES `location` (`LocationID`) ON DELETE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stocklevel`
--

LOCK TABLES `stocklevel` WRITE;
/*!40000 ALTER TABLE `stocklevel` DISABLE KEYS */;
INSERT INTO `stocklevel` VALUES (1,1,2,50,10),(2,2,3,200,50),(3,3,4,75,20),(4,4,5,5,2),(5,5,6,30,15),(6,3,1,50,10),(7,6,6,200,50),(8,7,5,75,20),(9,9,3,5,2),(10,10,6,30,15);
/*!40000 ALTER TABLE `stocklevel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction` (
  `TransactionID` int NOT NULL AUTO_INCREMENT,
  `AssetID` int DEFAULT NULL,
  `UserID` int DEFAULT NULL,
  `TransactionType` enum('Check-Out','Check-In','Transfer') NOT NULL,
  `TransactionDate` date NOT NULL,
  `DueDate` date DEFAULT NULL,
  PRIMARY KEY (`TransactionID`),
  KEY `AssetID` (`AssetID`),
  KEY `UserID` (`UserID`),
  CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`AssetID`) REFERENCES `asset` (`AssetID`) ON DELETE CASCADE,
  CONSTRAINT `transaction_ibfk_2` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`) ON DELETE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
INSERT INTO `transaction` VALUES (1,3,2,'Check-Out','2025-05-20','2025-06-20'),(2,2,2,'Check-Out','2025-05-15','2025-06-15'),(3,4,3,'Check-Out','2025-04-10','2025-05-10'),(4,7,2,'Check-In','2025-05-22','2025-06-21'),(5,9,2,'Check-Out','2025-05-21','2025-06-21'),(6,8,3,'Check-In','2025-05-22','2025-06-21'),(7,10,1,'Transfer','2025-05-18','2025-06-17');
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `UserID` int NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(25) NOT NULL,
  `LastName` varchar(25) NOT NULL,
  `Role` enum('Student','Faculty','Staff') NOT NULL,
  PRIMARY KEY (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'John','Doe','Student'),(2,'Jane','Smith','Faculty'),(3,'Alice','Johnson','Staff'),(4,'Bob','Williams','Student'),(5,'Emma','Brown','Faculty'),(6,'Mike','Davis','Staff');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-26 16:56:45
