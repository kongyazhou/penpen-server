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

## 开发环境

```
程序的开发和调试是在Windows7下进行的，简单介绍下windows下开发环境搭建的步骤。
```

#### 软件版本

- **python**

使用版本:3.5.1

查询命令:python -V (注意是大薇)

- **websocketd**

使用版本:0.2.12-windows_amd64

查询命令:websocketd -version

- **go**

使用版本:1.5.3

查询命令:go version

#### 开发环境搭建步骤

- 下载并安装[Python3](https://www.python.org/)
- 配置系统环境变量，在Path中添上Python3和Python3\Scripts\的路径
- 下载并安装[Go](http://www.golang.org/)语言运行环境(需要翻墙)
- 在Path中添上go\bin
- 下载并安装[Websocketd](http://websocketd.com/)
- 配系统环境变量，添上Websocketd的路径
- 在cmd下分别尝试查询上述软件版本，能显示即可


## 运行环境(稍后补充)

```
服务器的环境是操作系统CentOS 6.5内核版本Linux 2.6.32
```

#### 运行环境搭建步骤

安装Python

- 搭建Websocketd环境


## 部署步骤

将开发好的Pyhton服务器程序拷贝到服务器上

执行websocketd --port=端口号 python 程序名.py

## 相关网站

Python官网：[https://www.python.org/](https://www.python.org/)

Websocketd官网：[http://websocketd.com/](http://websocketd.com/)

Go官网：[http://www.golang.org/](http://www.golang.org/)
