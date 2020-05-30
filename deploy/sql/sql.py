# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    

usage:
    

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/1/16"
    __mail__ = "mingliang.gao@163.com"
------------------------------------------------
"""

"""
-- create user
CREATE TABLE `blog`.`sysuser` (
	`id` int NOT NULL AUTO_INCREMENT,
	`rtx_id` varchar(30),
	`fullname` varchar(50),
	`password` varchar(50),
	`email` varchar(50),
	`phone` varchar(30),
	`is_admin` bool,
	PRIMARY KEY (`id`)
) COMMENT='';

-- insert user
insert into blog.sysuser(rtx_id, fullname,password,email ,phone,is_admin) 
VALUES('admin', '系统管理员', '1', 'xxxxxx@163.com', '13011112222', 1);


-- create employee
CREATE TABLE `blog`.`employee` (
	`id` int NOT NULL AUTO_INCREMENT,
	`china_name` varchar(30),
	`english_name` varchar(30),
	`age` int,
	`sex` varchar(5),
	`birth_date` date,
	`email` varchar(30),
	`phone` varchar(30),
	`education` varchar(10),
	`birth_place` varchar(50),
	`card_id` varchar(100),
	`native_place` varchar(50),
	PRIMARY KEY (`id`)
) COMMENT='';

-- insert employee
insert into blog.employee(china_name, english_name, age, birth_date,sex,email,phone,education,birth_place,card_id,native_place)
VALUES
('张三', 'zhangsan', 30, '1990-03-06', 'M','zhangsan@163.com', '13911112222', '本科', '内蒙古通辽市', '150xxxxxxxxxxxxxx0', '内蒙古通辽市'),
('李四', 'lisi', 28, '1992-12-11', 'M', 'lisi@163.com', '13911112222', '研究生', '内蒙古通辽市', '151xxxxxxxxxxxxxx1', '内蒙古通辽市'),
('朱五️', 'zhuwu', 31, '1989-06-27','M', 'zhuwu@163.com', '13711112222', '博士', '内蒙古通辽市', '152xxxxxxxxxxxxxx2', '内蒙古通辽市'),
('赵六', 'zhaoliu', 40, '1980-11-18','F', 'zhaoliu@163.com', '13611112222', '本科', '内蒙古通辽市', '153xxxxxxxxxxxxxx3', '内蒙古通辽市'),
('一', 'yi', 30, '1990-03-06', 'M','yi@163.com', '13911112201', '本科', '内蒙古通辽市', '150xxxxxxxxxxxxxx1', '内蒙古通辽市'),
('二', 'er', 28, '1992-12-11', 'M', 'er@163.com', '13911112202', '研究生', '内蒙古通辽市', '151xxxxxxxxxxxxxx2', '内蒙古通辽市'),
('三', 'san', 31, '1989-06-27','M', 'san@163.com', '13711112203', '博士', '内蒙古通辽市', '152xxxxxxxxxxxxxx3', '内蒙古通辽市'),
('四', 'si', 40, '1980-11-18','F', 'si@163.com', '13611112204', '本科', '内蒙古通辽市', '153xxxxxxxxxxxxxx4', '内蒙古通辽市'),
('五', 'wu', 30, '1990-03-06', 'M','wu@163.com', '13911112205', '本科', '内蒙古通辽市', '150xxxxxxxxxxxxxx5', '内蒙古通辽市'),
('六', 'liu', 28, '1992-12-11', 'M', 'liu@163.com', '13911112206', '研究生', '内蒙古通辽市', '151xxxxxxxxxxxxxx6', '内蒙古通辽市'),
('七', 'qi', 31, '1989-06-27','M', 'qi@163.com', '13711112207', '博士', '内蒙古通辽市', '152xxxxxxxxxxxxxx7', '内蒙古通辽市'),
('八', 'ba', 40, '1980-11-18','F', 'ba@163.com', '13611112208', '本科', '内蒙古通辽市', '153xxxxxxxxxxxxxx8', '内蒙古通辽市'),
('九', 'jiu', 30, '1990-03-06', 'M','jiu@163.com', '13911112209', '本科', '内蒙古通辽市', '150xxxxxxxxxxxxxx9', '内蒙古通辽市'),
('十', 'shi', 28, '1992-12-11', 'M', 'shi@163.com', '13911112210', '研究生', '内蒙古通辽市', '151xxxxxxxxxxxxx10', '内蒙古通辽市'),
('十一', 'shiyi', 31, '1989-06-27','M', 'shiyi@163.com', '13711112211', '博士', '内蒙古通辽市', '152xxxxxxxxxxxxx11', '内蒙古通辽市'),
('十二', 'zhaoliu', 40, '1980-11-18','F', 'shier@163.com', '13611112212', '本科', '内蒙古通辽市', '153xxxxxxxxxxxxx12', '内蒙古通辽市'),
('十三', 'zhangsan', 30, '1990-03-06', 'M','shisan@163.com', '13911112213', '本科', '内蒙古通辽市', '150xxxxxxxxxxxxx13', '内蒙古通辽市'),
('十四', 'lisi', 28, '1992-12-11', 'M', 'shisi@163.com', '13911112214', '研究生', '内蒙古通辽市', '151xxxxxxxxxxxxx14', '内蒙古通辽市'),
('十五', 'shiwu', 31, '1989-06-27','M', 'shiwu@163.com', '13711112215', '博士', '内蒙古通辽市', '152xxxxxxxxxxxxx15', '内蒙古通辽市'),
('十六', 'shiiu', 40, '1980-11-18','F', 'shiliu@163.com', '13611112216', '本科', '内蒙古通辽市', '153xxxxxxxxxxxxx16', '内蒙古通辽市'),
('十七', 'shiqi', 30, '1990-03-06', 'M','shiqi@163.com', '13911112217', '本科', '内蒙古通辽市', '150xxxxxxxxxxxxx17', '内蒙古通辽市'),
('十八', 'shiba', 28, '1992-12-11', 'M', 'shiba@163.com', '13911112218', '研究生', '内蒙古通辽市', '151xxxxxxxxxxxxx18', '内蒙古通辽市'),
('十九', 'shijiu', 31, '1989-06-27','M', 'shijiu@163.com', '13711112219', '博士', '内蒙古通辽市', '152xxxxxxxxxxxxx19', '内蒙古通辽市'),
('二十', 'ershi', 40, '1980-11-18','F', 'ershi@163.com', '13611112220', '本科', '内蒙古通辽市', '153xxxxxxxxxxxxx20', '内蒙古通辽市'),
('二十一', 'ershiyi', 30, '1990-03-06', 'M','ershiyi@163.com', '13911112221', '本科', '内蒙古通辽市', '150xxxxxxxxxxxxx21', '内蒙古通辽市'),
('二十二', 'ershier', 28, '1992-12-11', 'M', 'ershier@163.com', '13911112222', '研究生', '内蒙古通辽市', '151xxxxxxxxxxxxx22', '内蒙古通辽市'),
('二十三', 'ershisan', 31, '1989-06-27','M', 'ershisan@163.com', '13711112223', '博士', '内蒙古通辽市', '152xxxxxxxxxxxxx23', '内蒙古通辽市'),
('二十四', 'ershisi', 40, '1980-11-18','F', 'ershisi@163.com', '13611112224', '本科', '内蒙古通辽市', '153xxxxxxxxxxxxx24', '内蒙古通辽市'),
('二十五', 'ershiwu', 30, '1990-03-06', 'M','ershiwu@163.com', '13911112225', '本科', '内蒙古通辽市', '150xxxxxxxxxxxxx25', '内蒙古通辽市'),
('二十六', 'ershiliu', 28, '1992-12-11', 'M', 'ershiliu@163.com', '13911112226', '研究生', '内蒙古通辽市', '151xxxxxxxxxxxxx26', '内蒙古通辽市'),
('二十七', 'ershiqi', 31, '1989-06-27','M', 'ershiqi@163.com', '13711112227', '博士', '内蒙古通辽市', '152xxxxxxxxxxxxx27', '内蒙古通辽市'),
('二十八', 'ershiba', 40, '1980-11-18','F', 'ershiba@163.com', '13611112228', '本科', '内蒙古通辽市', '153xxxxxxxxxxxxx28', '内蒙古通辽市'),
('二十九', 'ershijiu', 30, '1990-03-06', 'M','ershijiu@163.com', '13911112229', '本科', '内蒙古通辽市', '150xxxxxxxxxxxxx29', '内蒙古通辽市'),
('三十', 'sanshi', 28, '1992-12-11', 'M', 'sanshi@163.com', '13911112230', '研究生', '内蒙古通辽市', '151xxxxxxxxxxxxx30', '内蒙古通辽市'),
('三十一', 'sanshiyi', 31, '1989-06-27','M', 'sanshiyi@163.com', '13711112231', '博士', '内蒙古通辽市', '152xxxxxxxxxxxxx31', '内蒙古通辽市'),
('三十二', 'sanshier', 40, '1980-11-18','F', 'sanshier@163.com', '13611112232', '本科', '内蒙古通辽市', '153xxxxxxxxxxxxx32', '内蒙古通辽市'),
('三十三', 'sanhisan', 30, '1990-03-06', 'M','sanshisan@163.com', '13911112233', '本科', '内蒙古通辽市', '150xxxxxxxxxxxxx33', '内蒙古通辽市'),
('三十四', 'sanshisi', 28, '1992-12-11', 'M', 'sanshisi@163.com', '13911112234', '研究生', '内蒙古通辽市', '151xxxxxxxxxxxxx34', '内蒙古通辽市'),
('三十五', 'sanshiwu', 31, '1989-06-27','M', 'sanshiwu@163.com', '13711112235', '博士', '内蒙古通辽市', '152xxxxxxxxxxxxx35', '内蒙古通辽市'),
('三十六', 'sanshiliu', 40, '1980-11-18','F', 'sanshiliu@163.com', '13611112236', '本科', '内蒙古通辽市', '153xxxxxxxxxxxxx36', '内蒙古通辽市'),
('三十七', 'sanshiqi', 30, '1990-03-06', 'M','sanshiqi@163.com', '13911112237', '本科', '内蒙古通辽市', '150xxxxxxxxxxxxx37', '内蒙古通辽市'),
('三十八', 'sanshiba', 28, '1992-12-11', 'M', 'sanshiba@163.com', '13911112238', '研究生', '内蒙古通辽市', '151xxxxxxxxxxxxx38', '内蒙古通辽市'),
('三十九', 'sanshijiu', 31, '1989-06-27','M', 'sanshijiu@163.com', '137111122239', '博士', '内蒙古通辽市', '152xxxxxxxxxxxxx39', '内蒙古通辽市'),
('四十', 'sishi', 28, '1992-12-11', 'M', 'sishi@163.com', '13911112240', '研究生', '内蒙古通辽市', '151xxxxxxxxxxxxx40', '内蒙古通辽市'),
('四十一', 'sishiyi', 31, '1989-06-27','M', 'sishiyi@163.com', '13711112241', '博士', '内蒙古通辽市', '152xxxxxxxxxxxxx41', '内蒙古通辽市'),
('四十二', 'sishier', 40, '1980-11-18','F', 'sishier@163.com', '13611112242', '本科', '内蒙古通辽市', '153xxxxxxxxxxxxx42', '内蒙古通辽市'),
('四十三', 'sishisan', 30, '1990-03-06', 'M','sishisan@163.com', '13911112243', '本科', '内蒙古通辽市', '150xxxxxxxxxxxxx43', '内蒙古通辽市'),
('四十四', 'sishisi', 28, '1992-12-11', 'M', 'sishishi@163.com', '13911112244', '研究生', '内蒙古通辽市', '151xxxxxxxxxxxxx44', '内蒙古通辽市'),
('四十五', 'sishiwu', 31, '1989-06-27','M', 'sishiwu@163.com', '13711112245', '博士', '内蒙古通辽市', '152xxxxxxxxxxxxx45', '内蒙古通辽市'),
('四十六', 'sishiliu', 40, '1980-11-18','F', 'sishiliu@163.com', '13611112246', '本科', '内蒙古通辽市', '153xxxxxxxxxxxxx46', '内蒙古通辽市'),
('四十七', 'sishiqi', 30, '1990-03-06', 'M','sishiqi@163.com', '13911112247', '本科', '内蒙古通辽市', '150xxxxxxxxxxxxx47', '内蒙古通辽市'),
('四十八', 'sishiba', 28, '1992-12-11', 'M', 'sishiba@163.com', '13911112248', '研究生', '内蒙古通辽市', '151xxxxxxxxxxxxx48', '内蒙古通辽市'),
('四十九', 'sishijiu', 31, '1989-06-27','M', 'sishijiu@163.com', '13711112249', '博士', '内蒙古通辽市', '152xxxxxxxxxxxxx49', '内蒙古通辽市'),
('五十', 'wushi', 40, '1980-11-18','F', 'wushi@163.com', '13611112250', '本科', '内蒙古通辽市', '153xxxxxxxxxxxxx50', '内蒙古通辽市');









"""




