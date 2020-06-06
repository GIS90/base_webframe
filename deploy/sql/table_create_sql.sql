------------------------------------------------
describe:
    create table sql

    tables:
        sysuser
        enums
        employee

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
	`rtx_id` varchar(30) not null COMMENT 'rtx标识',
	`fullname` varchar(50) not null COMMENT '名称',
	`password` varchar(50) not null COMMENT '密码',
	`email` varchar(50)  COMMENT '邮箱',
	`phone` varchar(30)  COMMENT '电话',
	`image` varchar(255)  COMMENT '头像',
	`is_admin` bool  COMMENT '是否管理员权限',
	PRIMARY KEY (`id`),
	UNIQUE INDEX phone(id ASC),
) COMMENT='';


-- create employee

DROP TABLES IF EXISTS `employee`;

CREATE TABLE `blog`.`employee` (
	`id` int NOT NULL AUTO_INCREMENT,
	`china_name` varchar(30) NOT NULL COMMENT '中文名称',
	`english_name` varchar(45) COMMENT '英文名称',
	`phone` varchar(20) NOT NULL COMMENT '电话',
	`email` varchar(30) COMMENT '邮箱',
	`sex` varchar(10)  COMMENT '性别',
	`birth_date` date COMMENT '出生日期',
	`political_status` varchar(10) COMMENT '政治面貌',
	`nation` varchar(10) COMMENT '民族',
	`nationality` varchar(10) COMMENT '国籍',
	`residence_type` varchar(10) COMMENT '户口类型',
	`education` varchar(10) COMMENT '教育程度',
	`marriage` varchar(10) COMMENT '婚姻状况',
	`card_type` varchar(30) COMMENT '证件类型',
	`card_id` varchar(30) NOT NULL COMMENT '证件号码',
	`card_deadline` date COMMENT '过期日期',
	`card_place` varchar(100) COMMENT '证件地址',
	`current_address` varchar(100) COMMENT '现住址',
	`bank_type` varchar(10) COMMENT '开户行',
	`bank_country` varchar(10) COMMENT '开户行国家',
	`bank_city` varchar(30) COMMENT '开户城市',
	`bank_id` varchar(30) COMMENT '工资卡号',
	`bank_name` varchar(30) COMMENT '开户姓名',
	`entry_date` date COMMENT '入职日期',
	`quit_date` date COMMENT '离职日期',
	`status` varchar(10) NOT NULL COMMENT '任职状态',
	`entry_submit_time` timestamp COMMENT '入职提交日期',
	`entry_submit_rtx` varchar(30) COMMENT '入职提交用户',
	`quit_submit_time` timestamp COMMENT '离职提交日期',
	`quit_submit_rtx` varchar(30) COMMENT '离职提交用户',
	`last_update_time` timestamp COMMENT '最后更新日期',
	`last_update_rtx` varchar(30) COMMENT '最后更新用户',

	PRIMARY KEY (`id`),
    UNIQUE INDEX phone(id ASC),
	UNIQUE INDEX card_id(id ASC)
) COMMENT='';

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