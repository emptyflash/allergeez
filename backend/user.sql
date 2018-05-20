CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) PRIMARY KEY AUTO_INCREMENT,
  `endpoint` varchar(255) DEFAULT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COMMENT='HACKATHON';

CREATE TABLE IF NOT EXISTS `subscriptions` (
  `id` int(11) PRIMARY KEY AUTO_INCREMENT,
  `threshold` varchar(15) NOT NULL,
  `allergen_name` varchar(255) NOT NULL,
  `user_id` int(11) NOT NULL REFERENCES users(id)
);
