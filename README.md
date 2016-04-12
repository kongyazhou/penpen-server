# penpen-server

* [概述](#概述)
* [开发环境](#开发环境)
* [运行环境](#运行环境)
* [部署步骤](#部署步骤)
* [相关网站](#相关网站)

## 概述

PenPen-Hybrid是一款面向企业用户的移动端IM应用。

penpen-server是项目的服务器端程序。

系统框架见[百度脑图](http://naotu.baidu.com/file/057cee4fc39355125d9fe58789efc154)。

PenPen服务器端采用Webscketd框架，程序用Python语言开发。

```
关于Websocketd以及相关学习资料，稍后将整理至Documentation的HybridApp中。
```

## 服务器端设计

包含以下几个守护线程：

1. 监听用户在线状态(客户端发心跳)类似看门狗
2. 接收对话文本消息
3. 接受注册信息
4. 拆包

系统设计见百度脑图。

## 开发环境

```
程序的开发和调试是在Windows7下进行的，简单介绍下windows下开发环境搭建的步骤。
```

#### 软件版本

- **python**

使用版本:3.4.4(由于Mysql connector的限制，最新只能使用3.4版本)

查询命令:python -V (注意是大薇)

- **websocketd**

使用版本:0.2.12-windows_amd64

查询命令:websocketd -version

- **go**

使用版本:1.5.3

查询命令:go version

- **mysql**

使用版本:????

查询命令:????

#### 开发环境搭建步骤

- 下载并安装[Python3](https://www.python.org/)
- 配置系统环境变量，在Path中添上Python3和Python3\Scripts\的路径
- 下载并安装[Go](http://www.golang.org/)语言运行环境(需要翻墙)
- 在Path中添上go\bin
- 下载并安装[Websocketd](http://websocketd.com/)
- 配系统环境变量，添上Websocketd的路径
- 在cmd下分别尝试查询上述软件版本，能显示即可

#### 开发工具

**sublime python插件**

[SublimeREPL](https://github.com/wuub/SublimeREPL)：运行调试Python程序

本机快捷键配置如下:

- ctrl+f5 运行当前python文件
- ctrl+f6 pdb调试当前python文件
- ctrl+f7 打开iPython命令行

更多配置快捷键方法，以及调试使用说明，请访问百度以及Github。

[Anaconda](https://github.com/DamnWidget/anaconda)：格式对齐，拼写检查，自动补充，提示等

## 服务器环境搭建

```
服务器的环境是操作系统CentOS 6.5内核版本Linux 2.6.32 x86机构64位系统
```

#### 安装Mysql

yum安装Mysql

```bash
yum install mysql mysql-server mysql-devel -y
```

启动mysql服务

```bash
service mysqld start
```

配置开机启动

```bash
(查看系统服务中有没有mysqld)
chkconfig --list | grep mysql*
(如果没有则添加mysqld服务)
chkconfig --add mysqld
(配置开机启动mysqld服务)
chkconfig mysqld on
```

设置root帐号密码

```bash
mysqladmin -u root password "newpass"
```

创建账号

```
CREATE USER 'penpen'@'%' IDENTIFIED BY 'a1s2D3F4G5';
```

授权

```
GRANT ALL PRIVILEGES ON *.* TO 'penpen'@'%' IDENTIFIED BY 'a1s2D3F4G5' WITH GRANT OPTION; flush privileges;
```

#### 安装Go环境

yum安装golang

```
rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
yum install golang -y
```

#### 搭建Websocketd环境

官网下载[websocketd](http://websocketd.com/)。

unzip ...

```
ln -s /usr/local/src/websocketd /usr/bin/websocketd
```

#### 安装Python3.4

1. **安装**

下载python3.4.4，建议放到/usr/local/src目录下，解压并安装：

```
tar -zxvf Python-XXX.tgz
cd Python-XXX
./configure
make && make install
```

2. **修改环境**

python环境(视情况而定)

```
mv /usr/bin/python /usr/bin/python_old
ln -s /usr/local/bin/python3 /usr/bin/python
```

修改yum

```
vi /usr/bin/yum
```

将

```
#!/usr/bin/python
```

改为:

```
#!/usr/bin/python2.6
```

3. **安装mysql-connector**

我安装的是平台无关版本

解压后执行安装操作

```
python setup.py install
```

4. **安装jpush**

下载jpush-api-python

```
python setup.py install
```

#### 安装apache

yum 安装httpd服务

```bash
yum install httpd -y
```

配置开机启动

```bash
chkconfig httpd on
```

启动服务

```bash
service httpd start  
```

如果还看不到网页，记得关掉防火墙=。=||

```bash
service iptables stop
```

#### 安装php

```bash
yum install php -y
```

安装PHP组件

```bash
yum install php-mysql php-gd libjpeg* php-ldap php-odbc php-pear php-xml php-xmlrpc php-mbstring php-bcmath php-mhash
```

vi /etc/httpd/conf/httpd.conf 

```
DirectoryIndex index.html 加上index.php
```

别忘了给upload文件夹加权限(┬＿┬)

```bash
chmod 777 upload 
```
配置
upload_tmp_dir = /var/www/temp/

#### 配置启动项

配置开机启动命令

修改/etc/rc.d/rc.local，使服务器开机执行服务器端程序

```bash
sudo websocketd --port=20888 python344 /home/ec2-user/penpen/20888.py &
sudo websocketd --port=21888 python344 /home/ec2-user/penpen/21888.py &
```

```bash
chmod +x /etc/rc.d/rc.local
```

#### AWS RedHat

由于华为云到期，不得不将开发调试工作搬到AWS上，一时手贱选了RedHat系统，结果为了一些小配置就花了两三天，记录一下。

AWS**密钥**生成

```bash
chmod 600 xxx.pem 
ssh-keygen -p -f xxx.pem 
ssh-keygen -e -f xxx.pem > xxx.pem.pub
```

**数据库**是mariaDB不是Mysql,安装mariaDB

```bash
yum -y install mariadb*
systemctl start mariadb
chkconfig mariadb on (等效于systemctl enable mariadb.service)
```

首先，RedHat7上的**防火墙**不是iptables而是SELinux

```
开发阶段为了方便暂时不考虑详细配置，直接关闭防火墙
```

查看防火墙状态：

```bash
/usr/sbin/sestatus -v
```

1、临时关闭（不用重启机器）：

```bash
setenforce 0 
```

2、修改配置文件需要重启机器：

修改/etc/selinux/config 文件

```bash
SELINUX=enforcing => SELINUX=disabled
```

重启机器即可

《[查看 SELinux状态及关闭SELinux](http://bguncle.blog.51cto.com/3184079/957315/)》

漫漫长路，遍地是坑。

## centos下 Apache、php、mysql默认安装路径

**apache**

如果采用RPM包安装，安装路径应在 /etc/httpd目录下

apache配置文件:/etc/httpd/conf/httpd.conf

Apache模块路径：/usr/sbin/apachectl

web目录:/var/www/html

如果采用源代码安装，一般默认安装在/usr/local/apache2目录下

**php**

如果采用RPM包安装，安装路径应在 /etc/目录下

php的配置文件:/etc/php.ini

如果采用源代码安装，一般默认安装在/usr/local/lib目录下

php配置文件: /usr/local/lib/php.ini或/usr/local/php/etc/php.ini

**mysql**

如果采用RPM包安装，安装路径应在/usr/share/mysql目录下

mysqldump文件位置：/usr/bin/mysqldump

mysql配置文件：/etc/my.cnf或/usr/share/mysql/my.cnf

mysql数据目录：/var/lib/mysql目录下

如果采用源代码安装，一般默认安装在/usr/local/mysql目录下

## 部署步骤

将开发好的Pyhton服务器程序拷贝到服务器上

执行websocketd --port=端口号 python 程序名.py


## 测试优化

[LINUX下查看CPU使用率的命令](http://www.cnblogs.com/Wen-Man/archive/2011/04/04/2373771.html)

## 相关网站

Python官网：[https://www.python.org/](https://www.python.org/)

Websocketd官网：[http://websocketd.com/](http://websocketd.com/)

Go官网：[http://www.golang.org/](http://www.golang.org/)

[廖雪峰Python3教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)

[初步理解Python进程的信号通讯](http://www.jb51.net/article/63787.htm)