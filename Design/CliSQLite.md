# Sqlite

```
当前设计着重解决消息存储，读取的策略
```

数据库名:penpen.user(例如：penpen.12345678900)

1. 一张lastMessage表，凡是有过聊天记录的联系人都建一条数据
2. 凡是在lastMessage内的联系人，都建有一张allMessage表，记录用户与该联系的所有聊天信息
3. 一张user表，记录所有联系人及其签名

#### lastMessage

表名：lastMessage

```
id(int)(主键)
user(text)(12345678900)
name(text)
icon(text)
lastMessage(text)
lastTime(text)
unreadNo(int)
```


#### lastGroupMessage

表名：lastGroupMessage

```
id(int)(主键)
gid(text)(1)
name(text)
lastMessage(text)
lastTime(text)
unreadNo(int)
```

#### allMessage

表名：penpen1234567890(user)

```
id(int)(主键)
isFromMe(int)
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

