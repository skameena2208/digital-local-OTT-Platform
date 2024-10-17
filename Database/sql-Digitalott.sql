/*
SQLyog Community v13.2.0 (64 bit)
MySQL - 8.0.33 : Database - ott_platformsss
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`ott_platformsss` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `ott_platformsss`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add admin login',7,'add_adminlogin'),
(26,'Can change admin login',7,'change_adminlogin'),
(27,'Can delete admin login',7,'delete_adminlogin'),
(28,'Can view admin login',7,'view_adminlogin'),
(29,'Can add category',8,'add_category'),
(30,'Can change category',8,'change_category'),
(31,'Can delete category',8,'delete_category'),
(32,'Can view category',8,'view_category'),
(33,'Can add contact',9,'add_contact'),
(34,'Can change contact',9,'change_contact'),
(35,'Can delete contact',9,'delete_contact'),
(36,'Can view contact',9,'view_contact'),
(37,'Can add customer',10,'add_customer'),
(38,'Can change customer',10,'change_customer'),
(39,'Can delete customer',10,'delete_customer'),
(40,'Can view customer',10,'view_customer'),
(41,'Can add movie',11,'add_movie'),
(42,'Can change movie',11,'change_movie'),
(43,'Can delete movie',11,'delete_movie'),
(44,'Can view movie',11,'view_movie'),
(45,'Can add movie_ review',12,'add_movie_review'),
(46,'Can change movie_ review',12,'change_movie_review'),
(47,'Can delete movie_ review',12,'delete_movie_review'),
(48,'Can view movie_ review',12,'view_movie_review'),
(49,'Can add notification',13,'add_notification'),
(50,'Can change notification',13,'change_notification'),
(51,'Can delete notification',13,'delete_notification'),
(52,'Can view notification',13,'view_notification'),
(53,'Can add serial_ review',14,'add_serial_review'),
(54,'Can change serial_ review',14,'change_serial_review'),
(55,'Can delete serial_ review',14,'delete_serial_review'),
(56,'Can view serial_ review',14,'view_serial_review'),
(57,'Can add serials',15,'add_serials'),
(58,'Can change serials',15,'change_serials'),
(59,'Can delete serials',15,'delete_serials'),
(60,'Can view serials',15,'view_serials'),
(61,'Can add subscription',16,'add_subscription'),
(62,'Can change subscription',16,'change_subscription'),
(63,'Can delete subscription',16,'delete_subscription'),
(64,'Can view subscription',16,'view_subscription'),
(65,'Can add webseries',17,'add_webseries'),
(66,'Can change webseries',17,'change_webseries'),
(67,'Can delete webseries',17,'delete_webseries'),
(68,'Can view webseries',17,'view_webseries'),
(69,'Can add webseries_ review',18,'add_webseries_review'),
(70,'Can change webseries_ review',18,'change_webseries_review'),
(71,'Can delete webseries_ review',18,'delete_webseries_review'),
(72,'Can view webseries_ review',18,'view_webseries_review'),
(73,'Can add serials_ episodes',19,'add_serials_episodes'),
(74,'Can change serials_ episodes',19,'change_serials_episodes'),
(75,'Can delete serials_ episodes',19,'delete_serials_episodes'),
(76,'Can view serials_ episodes',19,'view_serials_episodes'),
(77,'Can add subscribers',20,'add_subscribers'),
(78,'Can change subscribers',20,'change_subscribers'),
(79,'Can delete subscribers',20,'delete_subscribers'),
(80,'Can view subscribers',20,'view_subscribers'),
(81,'Can add episode',21,'add_episode'),
(82,'Can change episode',21,'change_episode'),
(83,'Can delete episode',21,'delete_episode'),
(84,'Can view episode',21,'view_episode');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'dreamapp','adminlogin'),
(8,'dreamapp','category'),
(9,'dreamapp','contact'),
(10,'dreamapp','customer'),
(21,'dreamapp','episode'),
(11,'dreamapp','movie'),
(12,'dreamapp','movie_review'),
(13,'dreamapp','notification'),
(14,'dreamapp','serial_review'),
(15,'dreamapp','serials'),
(19,'dreamapp','serials_episodes'),
(20,'dreamapp','subscribers'),
(16,'dreamapp','subscription'),
(17,'dreamapp','webseries'),
(18,'dreamapp','webseries_review'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-09-02 12:50:01.241567'),
(2,'auth','0001_initial','2024-09-02 12:50:01.659285'),
(3,'admin','0001_initial','2024-09-02 12:50:01.754473'),
(4,'admin','0002_logentry_remove_auto_add','2024-09-02 12:50:01.770464'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-09-02 12:50:01.770464'),
(6,'contenttypes','0002_remove_content_type_name','2024-09-02 12:50:01.835197'),
(7,'auth','0002_alter_permission_name_max_length','2024-09-02 12:50:01.874815'),
(8,'auth','0003_alter_user_email_max_length','2024-09-02 12:50:01.882164'),
(9,'auth','0004_alter_user_username_opts','2024-09-02 12:50:01.898248'),
(10,'auth','0005_alter_user_last_login_null','2024-09-02 12:50:01.914715'),
(11,'auth','0006_require_contenttypes_0002','2024-09-02 12:50:01.930508'),
(12,'auth','0007_alter_validators_add_error_messages','2024-09-02 12:50:01.930508'),
(13,'auth','0008_alter_user_username_max_length','2024-09-02 12:50:01.962151'),
(14,'auth','0009_alter_user_last_name_max_length','2024-09-02 12:50:02.006308'),
(15,'auth','0010_alter_group_name_max_length','2024-09-02 12:50:02.012654'),
(16,'auth','0011_update_proxy_permissions','2024-09-02 12:50:02.012654'),
(17,'auth','0012_alter_user_first_name_max_length','2024-09-02 12:50:02.062328'),
(18,'dreamapp','0001_initial','2024-09-02 12:50:02.316532'),
(19,'sessions','0001_initial','2024-09-02 12:50:02.329524'),
(20,'dreamapp','0002_alter_customer_enddate_alter_customer_startdate','2024-09-02 12:52:00.766914'),
(21,'dreamapp','0003_alter_serials_duration','2024-09-05 04:50:40.318819');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('ps91n3fnrljtsv8vb4semj8qpcuh8knp','eyJlbWFpbCI6ImN1c3RvbWVyMUBnbWFpbC5jb20ifQ:1slM4f:FusOpIwJhszyBAfK140XWn50ZN-_BgB-55-Uz_8uVao','2024-09-17 05:27:29.932270'),
('tn7994cftkdhvpc0x68n8x039ad90ag3','eyJlbWFpbCI6ImN1c3RvbWVyQGdtYWlsLmNvbSJ9:1slLci:Vu8JEV7Au2LfO0eRi7K7-YwSIsTkwyKxnRCPP2mYIG8','2024-09-17 04:58:36.588272');

/*Table structure for table `dreamapp_adminlogin` */

DROP TABLE IF EXISTS `dreamapp_adminlogin`;

CREATE TABLE `dreamapp_adminlogin` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dreamapp_adminlogin` */

insert  into `dreamapp_adminlogin`(`id`,`email`,`password`) values 
(1,'admin@gmail.com','123');

/*Table structure for table `dreamapp_category` */

DROP TABLE IF EXISTS `dreamapp_category`;

CREATE TABLE `dreamapp_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dreamapp_category` */

insert  into `dreamapp_category`(`id`,`title`) values 
(1,'Devotinal'),
(2,'Science Freq');

/*Table structure for table `dreamapp_contact` */

DROP TABLE IF EXISTS `dreamapp_contact`;

CREATE TABLE `dreamapp_contact` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `subject` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dreamapp_contact` */

insert  into `dreamapp_contact`(`id`,`message`,`name`,`email`,`subject`) values 
(1,'Hi','Praveena Fashions','vendor@gmail.com','Ott'),
(2,'Hi','SATYA PHANEENDRA VARMA RUDRARAJU','vendor@gmail.com','hi');

/*Table structure for table `dreamapp_customer` */

DROP TABLE IF EXISTS `dreamapp_customer`;

CREATE TABLE `dreamapp_customer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `gender` varchar(40) NOT NULL,
  `age` int NOT NULL,
  `mobile` bigint NOT NULL,
  `address` longtext NOT NULL,
  `password` varchar(70) NOT NULL,
  `status` varchar(40) NOT NULL,
  `startdate` date DEFAULT NULL,
  `enddate` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dreamapp_customer` */

insert  into `dreamapp_customer`(`id`,`name`,`email`,`gender`,`age`,`mobile`,`address`,`password`,`status`,`startdate`,`enddate`) values 
(1,'SATYA PHANEENDRA VARMA RUDRARAJU','customer@gmail.com','Male',22,7989713677,'D-NO 6-212, Alluri vari veedi, Lakkavaram, Malikipuram Mandalam','123','Accepted','2024-09-05','2025-03-04'),
(2,'Radha','customer1@gmail.com','Male',22,7989713677,'D-NO 6-212, Alluri vari veedi, Lakkavaram, Malikipuram Mandalam','123','Accepted',NULL,NULL);

/*Table structure for table `dreamapp_episode` */

DROP TABLE IF EXISTS `dreamapp_episode`;

CREATE TABLE `dreamapp_episode` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `episode_number` int unsigned NOT NULL,
  `release_date` date NOT NULL,
  `thumbnail` varchar(100) NOT NULL,
  `video` varchar(100) NOT NULL,
  `webseries_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dreamapp_episode_webseries_id_8408e2f6_fk_dreamapp_webseries_id` (`webseries_id`),
  CONSTRAINT `dreamapp_episode_webseries_id_8408e2f6_fk_dreamapp_webseries_id` FOREIGN KEY (`webseries_id`) REFERENCES `dreamapp_webseries` (`id`),
  CONSTRAINT `dreamapp_episode_chk_1` CHECK ((`episode_number` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dreamapp_episode` */

insert  into `dreamapp_episode`(`id`,`title`,`description`,`episode_number`,`release_date`,`thumbnail`,`video`,`webseries_id`) values 
(4,'Hanuman','hanuman Moral stories',1,'2024-09-06','1646574-h-94192d7ae6fd_WmHSs7x.webp','hanuman.mp4',4);

/*Table structure for table `dreamapp_movie` */

DROP TABLE IF EXISTS `dreamapp_movie`;

CREATE TABLE `dreamapp_movie` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(60) NOT NULL,
  `category` longtext NOT NULL,
  `cast` varchar(40) NOT NULL,
  `description` longtext NOT NULL,
  `director` varchar(60) NOT NULL,
  `duration` bigint NOT NULL,
  `release_date` date NOT NULL,
  `language` varchar(60) NOT NULL,
  `thumbnail` varchar(100) NOT NULL,
  `movie_video` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dreamapp_movie` */

insert  into `dreamapp_movie`(`id`,`title`,`category`,`cast`,`description`,`director`,`duration`,`release_date`,`language`,`thumbnail`,`movie_video`) values 
(1,'kaliki2898','Science Freq','Prabhas, Amithab,Kamal Hassan','A modern avatar of the Hindu god Vishnu, is said to have descended on Earth to protect the world from evil forces.','Nag Ashwin',176000000,'2024-09-04','Telugu,Hindi,English,Tamil,Kanada','kaliki_Tpzs789.jpg','Kalki-2898-AD-Telugu-ryz2c-2024_q0FQax3.mp4'),
(3,'Bahubali','History','Prabhas, Rana, Anushka','Kingdom','SS Rajamouli',144000000,'2024-09-12','Telugu,Hindi,English,Tamil,Kanada','bb1_DAuLHkh.jpg','bahubali1.mp4'),
(4,'Salaar','Friendship','Prabhas, Sruthi Hassan','Movie','Prasanth Neel',235000000,'2024-09-20','Telugu,Hindi,English,Tamil,Kanada','salarpic.jpg','salaar.mp4');

/*Table structure for table `dreamapp_movie_review` */

DROP TABLE IF EXISTS `dreamapp_movie_review`;

CREATE TABLE `dreamapp_movie_review` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(400) NOT NULL,
  `customer_email` varchar(254) NOT NULL,
  `date` datetime(6) NOT NULL,
  `review` varchar(150) NOT NULL,
  `rating` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dreamapp_movie_review` */

/*Table structure for table `dreamapp_notification` */

DROP TABLE IF EXISTS `dreamapp_notification`;

CREATE TABLE `dreamapp_notification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `title` varchar(70) NOT NULL,
  `description` longtext NOT NULL,
  `date_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dreamapp_notification` */

insert  into `dreamapp_notification`(`id`,`email`,`title`,`description`,`date_time`) values 
(1,'ed@gmail.com','m,qewwwee','hello Customers','2024-09-04 05:02:49.263115');

/*Table structure for table `dreamapp_serial_review` */

DROP TABLE IF EXISTS `dreamapp_serial_review`;

CREATE TABLE `dreamapp_serial_review` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(400) NOT NULL,
  `customer_email` varchar(254) NOT NULL,
  `date` datetime(6) NOT NULL,
  `review` varchar(150) NOT NULL,
  `rating` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dreamapp_serial_review` */

/*Table structure for table `dreamapp_serials` */

DROP TABLE IF EXISTS `dreamapp_serials`;

CREATE TABLE `dreamapp_serials` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `cast` varchar(50) NOT NULL,
  `duration` bigint NOT NULL,
  `description` longtext NOT NULL,
  `director` varchar(50) NOT NULL,
  `language` varchar(50) NOT NULL,
  `thumbnail` varchar(100) NOT NULL,
  `episode` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dreamapp_serials` */

insert  into `dreamapp_serials`(`id`,`title`,`cast`,`duration`,`description`,`director`,`language`,`thumbnail`,`episode`) values 
(1,'Brahmamudi','Deepika Rangaraju Manas Nagulapalli',182000000,'When the mother of three beautiful and talented daughters plans their wedding with suitors from an affluent family, situations take an unusual turn.','Aditya Mandal','Telugu','serialbm_1qDENC5.jpg','serialbm2_T8ZqrfX.jpg');

/*Table structure for table `dreamapp_serials_episodes` */

DROP TABLE IF EXISTS `dreamapp_serials_episodes`;

CREATE TABLE `dreamapp_serials_episodes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `video` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `episode_number` int NOT NULL,
  `serial_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dreamapp_serials_epi_serial_id_38f4404d_fk_dreamapp_` (`serial_id`),
  CONSTRAINT `dreamapp_serials_epi_serial_id_38f4404d_fk_dreamapp_` FOREIGN KEY (`serial_id`) REFERENCES `dreamapp_serials` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dreamapp_serials_episodes` */

insert  into `dreamapp_serials_episodes`(`id`,`title`,`video`,`description`,`episode_number`,`serial_id`) values 
(3,'Brahmamudi','episodes/serialvideo1_kOCRC1U.mp4','When the mother of three beautiful and talented daughters plans their wedding with suitors from an affluent family, situations take an unusual turn.',1,1),
(4,'Brahmamudi','episodes/serialvideo2.mp4','When the mother of three beautiful and talented daughters plans their wedding with suitors from an affluent family, situations take an unusual turn.',2,1);

/*Table structure for table `dreamapp_subscribers` */

DROP TABLE IF EXISTS `dreamapp_subscribers`;

CREATE TABLE `dreamapp_subscribers` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customer_email` varchar(254) NOT NULL,
  `startdate` date NOT NULL,
  `enddate` date NOT NULL,
  `holder_name` varchar(100) NOT NULL,
  `card_number` bigint NOT NULL,
  `cvv_number` bigint NOT NULL,
  `bank_name` varchar(100) NOT NULL,
  `subscription_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dreamapp_subscribers_subscription_id_db5607c5_fk_dreamapp_` (`subscription_id`),
  CONSTRAINT `dreamapp_subscribers_subscription_id_db5607c5_fk_dreamapp_` FOREIGN KEY (`subscription_id`) REFERENCES `dreamapp_subscription` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dreamapp_subscribers` */

insert  into `dreamapp_subscribers`(`id`,`customer_email`,`startdate`,`enddate`,`holder_name`,`card_number`,`cvv_number`,`bank_name`,`subscription_id`) values 
(1,'customer@gmail.com','2024-09-02','2024-12-01','Phani Varma',123456789123,227,'state bank of india',1);

/*Table structure for table `dreamapp_subscription` */

DROP TABLE IF EXISTS `dreamapp_subscription`;

CREATE TABLE `dreamapp_subscription` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `title` varchar(100) NOT NULL,
  `months` int NOT NULL,
  `cost` bigint NOT NULL,
  `discount` bigint NOT NULL,
  `date_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dreamapp_subscription` */

insert  into `dreamapp_subscription`(`id`,`email`,`title`,`months`,`cost`,`discount`,`date_time`) values 
(1,'admin@gmail.com','3 Months plan',3,350,50,'2024-09-02 15:12:04.487564'),
(2,'admin@gmail.com','Half- year Plan',6,650,50,'2024-09-04 04:26:37.125875'),
(3,'admin@gmail.com','Yearly Plan',12,1200,200,'2024-09-04 04:29:42.604107'),
(4,'admin@gmail.com','2 months Plan',2,400,20,'2024-09-04 04:38:00.137718');

/*Table structure for table `dreamapp_webseries` */

DROP TABLE IF EXISTS `dreamapp_webseries`;

CREATE TABLE `dreamapp_webseries` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `cast` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `duration` bigint NOT NULL,
  `director` varchar(255) NOT NULL,
  `release_date` date NOT NULL,
  `language` varchar(50) NOT NULL,
  `thumbnail` varchar(100) NOT NULL,
  `webseries_video` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dreamapp_webseries` */

insert  into `dreamapp_webseries`(`id`,`title`,`category`,`cast`,`description`,`duration`,`director`,`release_date`,`language`,`thumbnail`,`webseries_video`) values 
(4,'Hanuman','Devotional','Hanuman,Sri Ram, Lakshman, Sita','Hanuman Moral stories',172000000,'Phani Varma','2024-09-06','Telugu,Hindi,English,Tamil,Kanada','thumbnails/1646574-h-94192d7ae6fd_LhNnjsf.webp','1646574-h-94192d7ae6fd_h2Vwo2G.webp');

/*Table structure for table `dreamapp_webseries_review` */

DROP TABLE IF EXISTS `dreamapp_webseries_review`;

CREATE TABLE `dreamapp_webseries_review` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(400) NOT NULL,
  `customer_email` varchar(254) NOT NULL,
  `date` datetime(6) NOT NULL,
  `review` varchar(150) NOT NULL,
  `rating` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dreamapp_webseries_review` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
