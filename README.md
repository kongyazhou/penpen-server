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

## 运行环境(稍后补充)

```
服务器的环境是操作系统CentOS 6.5内核版本Linux 2.6.32 x86机构64位系统
```

#### 运行环境搭建步骤

安装Python

- 搭建Websocketd环境


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