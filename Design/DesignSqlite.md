# Sqlite-design

## 插件

[Cordova-sqlite-storage](https://github.com/litehelpers/Cordova-sqlite-storage)

当前使用的版本(插件有些小BUG，一直在更新，谨慎升级)：

```
id = "cordova-sqlite-storage"
version = "0.8.5"
```

## 设计
 
```
当前设计着重解决消息存储，读取的策略
```

数据库名:penpen.user(例如：penpen.12345678900)

1. 一张lastMessage表，凡是有过聊天记录的联系人都建一条数据
2. 凡是在lastMessage内的联系人，都建有一张allMessage表，记录用户与该联系的所有聊天信息
3. 一张user表，记录所有联系人及其签名

#### lastMessage

```
包含单聊与群聊
```

表名：lastMessage

```
id(int)(主键)
user(text)(userID 或者 groupID)
name(text)
icon(text)
type(int)(0:contact message,1:group message)
lastMessage(text)
lastTime(datetime)
unreadNo(int)
```

#### contactMessage

表名：penpen12345678900(user)

```
id(int)(主键)
isFromMe(int)
type(int)
content(text)
time(text)
unread(预留，未使用)
```


#### groupMessage

表名：penpen10(10为gid)

```
id(int)(主键)
isFromMe(int)
user(text)
content(text)
time(text)
unread(预留，未使用)
```

