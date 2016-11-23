/*
Navicat MySQL Data Transfer

Source Server         : suse_mysql
Source Server Version : 50714
Source Host           : 4.1.15.49:3306
Source Database       : penpen

Target Server Type    : MYSQL
Target Server Version : 50714
File Encoding         : 65001

Date: 2016-11-23 12:04:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for 12345678900
-- ----------------------------
DROP TABLE IF EXISTS `12345678900`;
CREATE TABLE `12345678900` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from` bigint(20) DEFAULT NULL,
  `to` bigint(20) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` tinyint(4) DEFAULT NULL,
  `content` mediumtext,
  `unread` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=307 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for 12345678901
-- ----------------------------
DROP TABLE IF EXISTS `12345678901`;
CREATE TABLE `12345678901` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from` bigint(20) DEFAULT NULL,
  `to` bigint(20) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` tinyint(4) DEFAULT NULL,
  `content` mediumtext,
  `unread` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=255 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for 12345678902
-- ----------------------------
DROP TABLE IF EXISTS `12345678902`;
CREATE TABLE `12345678902` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from` bigint(20) DEFAULT NULL,
  `to` bigint(20) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` tinyint(4) DEFAULT NULL,
  `content` mediumtext,
  `unread` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=89 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for 12345678903
-- ----------------------------
DROP TABLE IF EXISTS `12345678903`;
CREATE TABLE `12345678903` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from` bigint(20) DEFAULT NULL,
  `to` bigint(20) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` tinyint(4) DEFAULT NULL,
  `content` mediumtext,
  `unread` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=74 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for 12345678904
-- ----------------------------
DROP TABLE IF EXISTS `12345678904`;
CREATE TABLE `12345678904` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from` bigint(20) DEFAULT NULL,
  `to` bigint(20) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` tinyint(4) DEFAULT NULL,
  `content` mediumtext,
  `unread` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for 12345678905
-- ----------------------------
DROP TABLE IF EXISTS `12345678905`;
CREATE TABLE `12345678905` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from` bigint(20) DEFAULT NULL,
  `to` bigint(20) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` tinyint(4) DEFAULT NULL,
  `content` mediumtext,
  `unread` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=87 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for 12345678906
-- ----------------------------
DROP TABLE IF EXISTS `12345678906`;
CREATE TABLE `12345678906` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from` bigint(20) DEFAULT NULL,
  `to` bigint(20) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` tinyint(4) DEFAULT NULL,
  `content` mediumtext,
  `unread` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=38 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for 12345678907
-- ----------------------------
DROP TABLE IF EXISTS `12345678907`;
CREATE TABLE `12345678907` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from` bigint(20) DEFAULT NULL,
  `to` bigint(20) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` tinyint(4) DEFAULT NULL,
  `content` mediumtext,
  `unread` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for 12345678908
-- ----------------------------
DROP TABLE IF EXISTS `12345678908`;
CREATE TABLE `12345678908` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from` bigint(20) DEFAULT NULL,
  `to` bigint(20) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` tinyint(4) DEFAULT NULL,
  `content` mediumtext,
  `unread` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=227 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for 12345678909
-- ----------------------------
DROP TABLE IF EXISTS `12345678909`;
CREATE TABLE `12345678909` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from` bigint(20) DEFAULT NULL,
  `to` bigint(20) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` tinyint(4) DEFAULT NULL,
  `content` mediumtext,
  `unread` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=387 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for 15228977313
-- ----------------------------
DROP TABLE IF EXISTS `15228977313`;
CREATE TABLE `15228977313` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from` bigint(20) DEFAULT NULL,
  `to` bigint(20) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` tinyint(4) DEFAULT NULL,
  `content` mediumtext,
  `unread` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for 15669910253
-- ----------------------------
DROP TABLE IF EXISTS `15669910253`;
CREATE TABLE `15669910253` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from` bigint(20) DEFAULT NULL,
  `to` bigint(20) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` tinyint(4) DEFAULT NULL,
  `content` mediumtext,
  `unread` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for broadcast
-- ----------------------------
DROP TABLE IF EXISTS `broadcast`;
CREATE TABLE `broadcast` (
  `title` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `summary` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for captcha
-- ----------------------------
DROP TABLE IF EXISTS `captcha`;
CREATE TABLE `captcha` (
  `user` varchar(255) DEFAULT NULL,
  `captcha` varchar(255) DEFAULT NULL,
  `time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS `department`;
CREATE TABLE `department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for group
-- ----------------------------
DROP TABLE IF EXISTS `group`;
CREATE TABLE `group` (
  `gid` int(11) NOT NULL AUTO_INCREMENT,
  `holder` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `member` mediumtext,
  PRIMARY KEY (`gid`)
) ENGINE=MyISAM AUTO_INCREMENT=96 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for job
-- ----------------------------
DROP TABLE IF EXISTS `job`;
CREATE TABLE `job` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `user` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `department` varchar(255) DEFAULT '1',
  `job` varchar(255) DEFAULT '3',
  `online` int(11) DEFAULT NULL,
  `state` tinyint(4) DEFAULT '0',
  `signing` varchar(255) DEFAULT '',
  `equipment` varchar(255) DEFAULT NULL,
  `captcha` varchar(255) DEFAULT NULL,
  `signupTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
