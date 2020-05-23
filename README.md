> ### 项目架构
项目基于python+flask+mysql+gunicorn+supervisor搭建
  - python 开发语言，基于python2
  - flask 使用的web框架
  - mysql 数据库
  - gunicorn web服务与进程
  - supervisor 项目启动、停止、重启等操作
项目主要运行于Linux系统上，本人使用Centos7.0

> ### 环境搭建
  - 服务器Centos7.0系统
  - mysql数据库安装与配置
  - 更新web配置文件：deploy/config.py，目前有mail、log、db配置
  - 安装项目运行的环境：python install_env.py，建立项目独立的运行环境，安装了virtualenv、python、gunicorn、安装包等操作，详情了解请参考代码
  - source .venv/bin/activate：激活项目环境
  - 启动项目：gunicorn -c etc/dev/gunicorn_dev.conf或者手动启动（下面有介绍）
  - 选做：安装supervisor && 项目加入supervisor进行管理，项目包含了supervisord配置文件&&项目supervisor配置文件

> ### 安装包

  - pip install -r requirements.txt

此程序运行于python2，其中requirements.txt项目所需要的包，已固定版本

> ### supervisor

管理项目进程的启动、停止、重启等操作
安装：pip install supervisor
配置：
  - dev：etc/dev/supervisor_base_webframe.conf
  - prod：etc/prod/supervisor_base_webframe.conf

> ### 管理gunicorn

负责web项目进程、服务
安装：pip install gunicorn
配置：
配置：
  - dev：etc/dev/gunicorn_dev.conf
  - prod：etc/prod/gunicorn_dev.conf

> ### 其他

base_webframe_start.bash、base_webframe_end.bash为手动方式进行项目启动与项目结束

> ### 手动启动

wsgi文件加入
app.run(host="0.0.0.0", port=11111, debug=True)
执行python wsgi.py

> ### 联系方式

* ***Github:*** https://github.com/GIS90

* ***Email:*** gaoming971366@163.com

* ***Blog:*** http://pygo2.cn

* ***WeChat:*** PyGo90


*** Enjoy the good lift everyday ！！！***

