-- phpMyAdmin SQL Dump
-- version 3.3.8.1
-- http://www.phpmyadmin.net
--
-- 主机: w.rdc.sae.sina.com.cn:3307
-- 生成日期: 2013 年 03 月 31 日 13:26
-- 服务器版本: 5.5.23
-- PHP 版本: 5.2.9

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `app_chinapython`
--

-- --------------------------------------------------------

--
-- 表的结构 `logs`
--

CREATE TABLE IF NOT EXISTS `logs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `log` text NOT NULL,
  `datetime` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=53 ;

--
-- 转存表中的数据 `logs`
--

INSERT INTO `logs` (`id`, `log`, `datetime`) VALUES
(50, '那估计', '2013-03-27-16:09:02'),
(51, '开发者的微信号：oZfN9jgzVGy0hckH4uIGCCEF2NAE 接收方的微信号：gh_41d883ddb465 发送时间：1364371886 发信类型：文本 ', '2013-03-27-16:11:26'),
(52, '开发者的微信号：oZfN9jgzVGy0hckH4uIGCCEF2NAE 接收方的微信号：gh_41d883ddb465 发送时间：1364372248 发信类型：文本 ', '2013-03-27-16:17:04'),
(48, '开发者的微信号：oZfN9jgzVGy0hckH4uIGCCEF2NAE 接收方的微信号：gh_41d883ddb465 发送时间：1364370047 发信类型：文本 发信内容:sssss', '2013-03-27-15:40:48'),
(49, '开发者的微信号：oZfN9jgzVGy0hckH4uIGCCEF2NAE 接收方的微信号：gh_41d883ddb465 发送时间：1364370134 发信类型：文本 发信内容:{''FromUserName'': ''oZfN9jgzVGy0hckH4uIGCCEF2NAE'', ''MsgId'': ''5859925105169137980'', ''ToUserName'': ''gh_41d883ddb465'', ''Content'': u''\\u4e86\\u4e86\\u4e86\\u4e86\\u4e86'', ''MsgType'': ''text'', ''CreateTime'': ''1364370134''}', '2013-03-27-15:41:50');

-- --------------------------------------------------------

--
-- 表的结构 `sessions`
--

CREATE TABLE IF NOT EXISTS `sessions` (
  `session_id` char(128) NOT NULL,
  `atime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `data` text,
  UNIQUE KEY `session_id` (`session_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `sessions`
--

INSERT INTO `sessions` (`session_id`, `atime`, `data`) VALUES
('980d52b4d4ee504cc8bf294032d03037cfa165d3', '2013-03-31 13:25:24', 'KGRwMQpTJ2lwJwpwMgpWMjIyLjMzLjgxLjE5CnAzCnNTJ3Nlc3Npb25faWQnCnA0ClMnOTgwZDUy\nYjRkNGVlNTA0Y2M4YmYyOTQwMzJkMDMwMzdjZmExNjVkMycKcDUKcy4=\n');

-- --------------------------------------------------------

--
-- 表的结构 `textmessage`
--

CREATE TABLE IF NOT EXISTS `textmessage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fromuser` varchar(200) NOT NULL,
  `touser` varchar(200) NOT NULL,
  `datetime` varchar(200) NOT NULL,
  `content` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;

--
-- 转存表中的数据 `textmessage`
--

INSERT INTO `textmessage` (`id`, `fromuser`, `touser`, `datetime`, `content`) VALUES
(1, 'oZfN9jgzVGy0hckH4uIGCCEF2NAE', 'gh_41d883ddb465', '2013-03-27-16:17:04', '了了了了了'),
(2, 'oZfN9jgzVGy0hckH4uIGCCEF2NAE', 'gh_41d883ddb465', '2013-03-27-16:18:22', '了了了了了'),
(3, 'oZfN9jgzVGy0hckH4uIGCCEF2NAE', 'gh_41d883ddb465', '2013-03-27-16:35:02', '模棱两可'),
(4, 'oZfN9jgzVGy0hckH4uIGCCEF2NAE', 'gh_41d883ddb465', '2013-03-27-16:38:59', '噢噢噢'),
(5, 'oZfN9jldlaUU--rbUKCtjETvWLMI', 'gh_41d883ddb465', '2013-03-29-13:17:53', '扫马枪');

-- --------------------------------------------------------

--
-- 表的结构 `todo`
--

CREATE TABLE IF NOT EXISTS `todo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(300) DEFAULT NULL,
  `finished` int(11) DEFAULT '0',
  `post_date` datetime DEFAULT NULL,
  `userid` int(11) NOT NULL,
  `detail` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=40 ;

--
-- 转存表中的数据 `todo`
--

INSERT INTO `todo` (`id`, `title`, `finished`, `post_date`, `userid`, `detail`) VALUES
(36, '测试2', 0, '2013-03-25 13:49:30', 1, '测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2'),
(38, '测试修改的第2功能', 0, '2013-03-31 13:21:35', 1, '测试OKchu999应该看不到'),
(39, '测试功能', 0, '2013-03-31 13:22:06', 2, '测试chu888应该看不到。');

-- --------------------------------------------------------

--
-- 表的结构 `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `id` int(9) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `password` varchar(64) NOT NULL,
  `login_count` int(10) unsigned NOT NULL DEFAULT '0',
  `last_login` int(10) unsigned NOT NULL DEFAULT '0',
  `email` varchar(64) DEFAULT NULL,
  `admin` tinyint(1) DEFAULT '0',
  `guest` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- 转存表中的数据 `users`
--

INSERT INTO `users` (`id`, `name`, `full_name`, `password`, `login_count`, `last_login`, `email`, `admin`, `guest`) VALUES
(1, 'chu888', 'chu888', 'chu888', 10, 20100101, 'chu888@gmail.com', 0, 1),
(2, 'chu999', 'chu999', 'chu999', 1, 1, 'chu999@gmail.com', 1, 1);
