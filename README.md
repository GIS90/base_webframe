[项目架构]
项目基于python+flask+mysql+gunicorn+supervisor搭建
  - python 开发语言，基于python2
  - flask 后台web框架
  - mysql 数据库
  - gunicorn web服务与进程
  - supervisor 项目启动、停止、重启等操作

[环境搭建]
  - 搭建mysql数据库
  - 更新web配置文件：deploy/config.py
  - 安装项目运行的环境：python install_env.py
  - 启动项目：gunicorn -c etc/dev/gunicorn_dev.conf或者手动启动（下面有介绍）
  - 安装supervisor && 项目加入supervisor进行管理

[安装包]
pip install -r requirements.txt
此程序运行于python2，其中requirements.txt项目所需要的包，已固定版本

[supervisor]
管理项目进程的启动、停止、重启等操作
安装：pip install supervisor
配置：supervisor_base_webframe.conf
开启了web服务，端口为11111

[管理gunicorn]
负责web项目进程、服务
安装：pip install gunicorn
配置：gunicorn.conf

[其他]
base_webframe_start.bash、base_webframe_end.bash为手动方式进行项目启动与项目结束

[手动启动]
wsgi文件加入
app.run(host="0.0.0.0", port=11111, debug=True)
执行python wsgi.py