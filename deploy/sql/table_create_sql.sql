------------------------------------------------
describe:
    create table sql

usage:


base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/5/30"
    __mail__ = "mingliang.gao@163.com"
------------------------------------------------


-- create user
DROP TABLES IF EXISTS `sysuser`;

CREATE TABLE `sysuser` (
	`id` int NOT NULL AUTO_INCREMENT,
	`rtx_id` varchar(30),
	`fullname` varchar(50),
	`password` varchar(50),
	`email` varchar(50),
	`phone` varchar(30),
	`is_admin` bool,
	PRIMARY KEY (`id`)
) COMMENT='';


-- create employee

DROP TABLES IF EXISTS `employee`;

CREATE TABLE `blog`.`employee` (
	`id` int NOT NULL AUTO_INCREMENT,
	`china_name` varchar(30) NOT NULL COMMENT '中文名称',
	`english_name` varchar(45) COMMENT '英文名称',
	`sex` varchar(10) NOT NULL COMMENT '性别',
	`birth_date` date NOT NULL COMMENT '出生日期',
	`political_status` varchar(10) NOT NULL COMMENT '政治面貌',
	`nation` varchar(10) NOT NULL COMMENT '民族',
	`nationality` varchar(10) NOT NULL COMMENT '国籍',
	`education` varchar(10) NOT NULL COMMENT '教育程度',
	`marriage` varchar(10) NOT NULL COMMENT '婚姻状况',
	`phone` varchar(20) NOT NULL COMMENT '电话',
	`email` varchar(30) NOT NULL COMMENT '邮箱',
	`card_type` varchar(30) NOT NULL COMMENT '证件类型',
	`card_id` varchar(30) NOT NULL COMMENT '证件号码',
	`card_place` varchar(100) NOT NULL COMMENT '证件地址',
	`card_deadline` date NOT NULL COMMENT '证件截止日期',
	`residence_type` varchar(10) NOT NULL COMMENT '户口类型',
	`current_address` varchar(100) NOT NULL COMMENT '现住址',
	`bank_type` varchar(10) NOT NULL COMMENT '开户行',
	`bank_country` varchar(10) NOT NULL COMMENT '开户行国家',
	`bank_city` varchar(10) NOT NULL COMMENT '开户城市',
	`bank_id` varchar(30) NOT NULL COMMENT '工资卡号',
	`bank_name` varchar(30) NOT NULL COMMENT '开户姓名',
	`entry_date` date NOT NULL COMMENT '入职日期',
	`quit_date` date COMMENT '离职日期',
	`status` varchar(10) NOT NULL COMMENT '任职状态',


	PRIMARY KEY (`id`)
) COMMENT='';


-- enums
DROP TABLES IF EXISTS `enums`;

CREATE TABLE `enums` (
	`id` int NOT NULL AUTO_INCREMENT,
	`subid` int NOT NULL,
	`type` varchar(10),
	`name` varchar(20),
	PRIMARY KEY (`id`)
) COMMENT='';