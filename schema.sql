CREATE DATABASE IF NOT EXISTS shoperone;

USE shoperone;

CREATE TABLE IF NOT EXISTS `user` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `password_hash` CHAR(64) CHARACTER SET latin1 NOT NULL,
  `picture_url` varchar(2000) CHARACTER SET latin1 NOT NULL,
  `bio` varchar(1023) NOT NULL,
  `date_created` int(10) unsigned NOT NULL,
  `date_modified` int(10) unsigned NOT NULL,
  `revision_id` int(10) unsigned NOT NULL default '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `listing` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `seller_id` int(10) unsigned NOT NULL,
  `location` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `seller_id` (`seller_id`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `transaction` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `buyer_id` int(10) unsigned NOT NULL,
  `seller_id` int(10) unsigned NOT NULL,
  `location` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `seller_id` (`seller_id`),
  KEY `buyer_id` (`buyer_id`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `queue` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `buyer_id` int(10) unsigned NOT NULL,
  `listing_id` int(10) unsigned NOT NULL,
  `date_added` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `buyer_id-date_added` (`buyer_id`, `date_added`)
) ENGINE=InnoDB;

