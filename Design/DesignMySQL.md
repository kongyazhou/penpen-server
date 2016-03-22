# DesignMySQL

## MySQL

包含以下数据库：

* 消息数据库(以每个用户的ID为名分别建立数据库，包括一张未读消息表)

```
服务器暂不存储消息，故暂时只为每个用户建立一张未读表
```
#### 基本需求

数据库名：penpen

1. 每个用户一张消息表，包含读否字段
2. 用户信息表(包含用户姓名、userID(即手机号）、在线状态、所在部门、个性签名、头像、登录密码[、设备信息]等信息)
3. 广播表

#### 消息表message

from	发送者ID(15228977313)
to		接受者ID(13506721360)
time	发送时间(字符串:20160322073200)
type	内容类型(0:文字，1:图片，2:语音)
content	发送内容(base64编码存储）
unread	是否读过(0:读过，1:未读)

#### 用户信息表

name		姓名(base64)
user		用户ID(即手机号)
password	登录密码(md5)
depart		部门(base64)
job			职位(base64)
online		在线(在线：PID，不在线：0)
icon		头像(文件名，base64)
signing		个性签名(base64)
equipment	设备(*)

#### 通知表

title	通知标题
type	通知类型(1:通知，2:新闻，3:公告)
summary	通知摘要
url		链接


