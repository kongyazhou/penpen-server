#!/usr/bin/env python3.4
# import jpush as jpush
# from conf import app_key, master_secret
import mysql.connector
import json
import os
import base64
import random
import time
import signal
import sms253
from sys import stdout
from sys import stdin


class handleMessage(object):

    """
    This module provides all kinds of ways to handle message.
    type:
        0       getMessage
        1       readMsg     readMsg from table
        2       sendMsg     sendMsg to client
        3       writeMsg    writeMsg
        6       sendSMS
        7       checkSignupUser
        20888   login
        21888   recvMsg
        26888   recvGroupMsg
        30666   signupSMS
        30888   signup
        31888   updateSigning
        33888   updateStatus
        50888   syncAllMessages
        51888   syncAllContacts
        53888   syncAllGroups
        60888   createGroup
        other   error
    """

    def __init__(self, handleType=66):
        self.type = handleType
        # self._jpush = jpush.JPush(app_key, master_secret)
        # self.push = self._jpush.create_push()
        if self.type == 0:
            self.getMsg()
        elif self.type == 1:
            self.readMsg()
        elif self.type == 2:
            self.sendMsg()
        elif self.type == 3:
            self.writeMsg()
        elif self.type == 6:
            self.sendSMS()
        elif self.type == 7:
            self.checkSignupUser()
        elif self.type == 8:
            self.createUser()
        elif self.type == 9:
            self.getAllContacts()
        elif self.type == 20888:
            self.login()
        elif self.type == 21888:
            self.recvMsg()
        elif self.type == 26888:
            self.recvGroupMsg()
        elif self.type == 30666:
            self.signupSMS()
        elif self.type == 30888:
            self.signup()
        elif self.type == 31888:
            self.updateSigning()
        elif self.type == 33888:
            self.updateStatus()
        elif self.type == 50888:
            self.syncAllMessages()
        elif self.type == 51888:
            self.syncAllContacts()
        elif self.type == 53888:
            self.syncAllGroups()
        elif self.type == 60888:
            self.createGroup()
        else:
            pass

    def __call__(self, handleType=66):
        self.__init__(handleType)

    def getMsg(self):
        jsonMsg = stdin.readline()
        self.msg = json.loads(jsonMsg)
        if self.checkVersion():
            pass
        else:
            self.wrongVersion()
        self.decodeMsg()

    def decodeMsg(self):
        """This function decode the package's body part to get the message."""
        if self.msg["head"] == 1100:
            self.msg = self.msg["body"]
        elif self.msg["head"] == 1110:
            self.msg = eval(str(base64.b64decode(self.msg["body"]), encoding="utf-8"))
        else:
            # TODO
            pass

    def sendSMS(self):
        sms253.send_sms(self.SMS, self.user)

    def checkVersion(self):
        if self.msg["tail"] == "PENPEN 1.0":
            return 1
        else:
            return 0

    def wrongVersion(self):
        # TODO*
        pass

    def openMysqlCur(self):
        # create Mysql cursor
        self.config = {
            'host': 'localhost',
            'port': 3306,
            'database': 'penpen',
            'user': 'root',
            'password': 'a1s2D3F4G5!',
            'charset': 'utf8',
            'use_unicode': True,
            'get_warnings': True,
        }
        self.cnx = mysql.connector.connect(**self.config)
        self.cur = self.cnx.cursor()

    def closeMysqlCur(self):
        self.cur.close()
        self.cnx.close()

    def sendMsg(self):
        self.codeMsg()
        print(self.msg)
        stdout.flush()

    def codeMsg(self):
        # code msg
        self.msg = str(self.msg)
        self.codeID = 1110
        self.msg = {"head": self.codeID, "body": str(base64.b64encode(bytes(self.msg, encoding="utf-8")), encoding="utf-8"), "tail": "PENPEN 1.0"}

    def readMsg(self):
        """Read message from host's unread table"""
        self.openMysqlCur()
        stmt_select = "SELECT `from`, `to`, `time`, `type`, `content`, `id` FROM `%s` WHERE unread=1 ORDER BY id" % (self.user,)
        self.cur.execute(stmt_select)
        readID = []
        for row in self.cur.fetchall():
            # TODO If string, take""
            self.msg = '{"from":"%s","to":"%s","time":"%s","type":%d,"content":"%s"}' % (row[0], row[1], row[2], row[3], row[4])
            readID.append((int(self.user), row[5]))
            self.sendMsg()
        # Change unread status to 0
        stmt_update = "UPDATE `%s` SET unread=0 WHERE id=%s"
        self.cur.executemany(stmt_update, tuple(readID))
        self.cnx.commit()
        self.closeMysqlCur()

    def recvMsg(self):
        """First get the message, then write it into Mysql."""
        # TODO check status if online write&send else write&push
        self.getMsg()
        self.getTarPID()
        self.writeMsg()
        if self.tarPID:
            # TOTEST
            os.kill(self.tarPID, signal.SIGCHLD)
            self.pushMsg()
        else:
            self.pushMsg()
            pass

    def recvGroupMsg(self):
        """First get the message, then write it into Mysql."""
        self.getMsg()
        self.groupGID = self.msg["to"]
        # get group members array by gid
        self.getGroupMembers()
        for member in self.groupMembers:
            # if member != self.msg["from"]:
            self.msg["to"] = member
            self.writeGroupMsg()
            if member != self.msg["from"]:
                self.getTarPID()
                if self.tarPID:
                    # TOTEST
                    try:
                        os.kill(self.tarPID, signal.SIGCHLD)
                        self.pushMsg()
                    except:
                        self.pushMsg()
                else:
                    self.pushMsg()
                    pass

    def getGroupMembers(self):
        # TODO
        self.openMysqlCur()
        stmt_select = "SELECT `member` FROM `group` WHERE gid=%s" % (self.groupGID,)
        self.cur.execute(stmt_select)
        self.groupMembers = self.cur.fetchone()[0].split(',')
        self.closeMysqlCur()
        pass

    def writeGroupMsg(self):
        self.openMysqlCur()
        self.getLocalTime()
        if self.msg["to"] != self.msg["from"]:
            pass
            stmt_insert = "INSERT INTO `%s`( `from`, `to`, `time`, `type`, `content`, `unread`)\
                VALUES(%s, '%s', '%s', '%s', '%s', %d)" % (self.msg["to"], self.msg["from"], self.groupGID, self.time, self.msg["type"], self.msg["content"], 1)
            self.cur.execute(stmt_insert)
        else:
            stmt_insert = "INSERT INTO `%s`( `from`, `to`, `time`, `type`, `content`, `unread`)\
                VALUES(%s, '%s', '%s', '%s', '%s', %d)" % (self.msg["to"], self.msg["from"], self.groupGID, self.time, self.msg["type"], self.msg["content"], 0)
            self.cur.execute(stmt_insert)
        self.closeMysqlCur()

    def writeMsg(self):
        """Write the message to target's unread table"""
        self.openMysqlCur()
        self.getLocalTime()
        # Add message to receiver's table
        stmt_insert = "INSERT INTO `%s`( `from`, `to`, `time`, `type`, `content`, `unread`)\
            VALUES('%s', '%s', '%s', '%s', '%s', %d)" % (self.msg["to"], self.msg["from"], self.msg["to"], self.time, self.msg["type"], self.msg["content"], 1)
        self.cur.execute(stmt_insert)
        # Add message to sender's table
        stmt_insert = "INSERT INTO `%s`( `from`, `to`, `time`, `type`, `content`, `unread`)\
            VALUES('%s', '%s', '%s', '%s', '%s', %d)" % (self.msg["from"], self.msg["from"], self.msg["to"], self.time, self.msg["type"], self.msg["content"], 0)
        self.cur.execute(stmt_insert)
        self.closeMysqlCur()

    def getTarPID(self):
        """Get the PID of target from OnlineStatus database."""
        self.openMysqlCur()
        stmt_select = "SELECT online FROM user WHERE user=%s" % (self.msg["to"],)
        self.cur.execute(stmt_select)
        self.tarPID = self.cur.fetchone()[0]
        self.closeMysqlCur()

    def pushMsg(self):
        # self.push.audience = jpush.audience(jpush.alias("penpen" + self.msg["to"]))
        # if int(self.msg["type"]) < 10:
        #     self.push.notification = jpush.notification(android=jpush.android(alert=str(base64.b64decode(self.msg["content"]), encoding="utf-8"), extras={'user':self.msg["from"]}))
        # else:
        #     self.push.notification = jpush.notification(android=jpush.android(alert=str(base64.b64decode(self.msg["content"]), encoding="utf-8"), extras={'user':self.groupGID}))
        # # self.push.options = {"title":"12345678908"}
        # self.push.platform = jpush.all_
        # self.push.send()
        pass

    def login(self):
        self.getMsg()
        self.user = self.msg["user"]
        if self.checkPassword():
            self.loginSuccess()
            pass
        else:
            self.loginFailed()
            return
        self.openMysqlCur()
        stmt_update = "UPDATE user SET online=%d WHERE user=%s" % (os.getpid(), self.user)
        self.cur.execute(stmt_update)
        self.closeMysqlCur()

    def signup(self):
        self.getMsg()
        self.user = self.msg["user"]
        if self.checkSignupCaptcha():
            self.openMysqlCur()
            stmt_update = "UPDATE user SET name='%s', password='%s' WHERE user=%s" % (self.msg["name"], self.msg["password"], self.user)
            self.cur.execute(stmt_update)
            stmt_create = "CREATE TABLE `%s` (`id` INT NOT NULL AUTO_INCREMENT key, `from` bigint, `to` bigint, `time` DATETIME, `type` tinyint, `content` mediumtext, `unread` tinyint)  ENGINE = MYISAM;" % (self.user)
            self.cur.execute(stmt_create)
            self.closeMysqlCur()
        else:
            pass
        self.msg = {"user": self.msg["user"], "status": self.status, "time": self.getLocalTime()}
        self.sendMsg()

    def checkSignupCaptcha(self):
        # TODO 验证码超时判断
        self.openMysqlCur()
        stmt_select = "SELECT captcha FROM user WHERE user=%s" % (self.user)
        self.cur.execute(stmt_select)
        self.captcha = self.cur.fetchone()[0]
        self.closeMysqlCur()
        if self.msg["captcha"] == self.captcha:
            self.status = 0
            return True
        else:
            self.status = 1
            return False

    def signupSMS(self):
        self.getMsg()
        self.user = self.msg["user"]
        if self.checkSignupUser():
            self.getCaptcha()
            self.writeSignupCaptcha()
            self.getSignupSMS()
            self.sendSMS()
        else:
            # TODO
            self.SMS = "您的账号已存在，若遗忘密码，请在点击忘记密码操作。"
            pass
        # self.msg = {"user": self.user, "status": self.status, "SMS": self.SMS, "time": self.getLocalTime()}
        self.msg = {"user": self.user, "status": self.status, "time": self.getLocalTime()}
        self.sendMsg()

    def checkSignupUser(self):
        # TODO
        self.openMysqlCur()
        stmt_select = "SELECT password FROM user WHERE user=%s" % (self.user)
        self.cur.execute(stmt_select)
        try:
            self.password = self.cur.fetchone()[0]
        except:
            self.status = 0
            return True
        else:
            self.status = 1
            return False
        finally:
            self.closeMysqlCur()

    def writeSignupCaptcha(self):
        self.openMysqlCur()
        stmt_insert = "INSERT INTO `user`( `user`, `captcha`, `signupTime`) VALUES('%s', '%s', '%s')" % (self.msg["user"], self.captcha, self.getLocalTime())
        self.cur.execute(stmt_insert)
        self.closeMysqlCur()

    def getSignupSMS(self):
        self.SMS = "【penpen】尊敬的用户，您的注册码是" + str(self.captcha) + "，注册码有效时间10分钟，请尽快使用。"
        return self.SMS

    def getCaptcha(self):
        self.captcha = int(random.uniform(1000, 9999))
        # self.captcha = 1234
        return self.captcha

    def checkPassword(self):
        try:
            self.openMysqlCur()
            stmt_select = "SELECT password FROM user WHERE user=%s" % (self.msg["user"],)
            self.cur.execute(stmt_select)
            self.password = self.cur.fetchone()[0]
        except:
            return False
        else:
            return self.msg["password"] == self.password
        finally:
            self.closeMysqlCur()

    def updateProfile(self):
        # TODO
        pass

    def logout(self):
        # TODO
        pass

    def getLocalTime(self):
        # America time
        # self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 3600 * 12))
        # China time
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        return self.time
        # seconds since 1970
        # self.time = int(time.time())

    # def createPush(self):
    #     _jpush = jpush.JPush(app_key, master_secret)
    #     self.push = _jpush.create_push()

    def loginSuccess(self):
        self.msg = '{"status":11}'
        self.sendMsg()
        time.sleep(2)
        self.readMsg()

    def loginFailed(self):
        self.msg = '{"status":12}'
        self.sendMsg()

    def syncAllMessages(self):
        # TODO
        self.getMsg()
        self.openMysqlCur()
        stmt_select = "SELECT `from`, `to`, `time`, `type`, `content` FROM `%s` WHERE `to`=%s OR `from`=%s ORDER BY id" % (self.msg["user"], self.msg["target"], self.msg["target"])
        self.cur.execute(stmt_select)
        self.msg = []
        for row in self.cur.fetchall():
            self.msg.append('{"from":"%s","to":"%s","time":"%s","type":%d,"content":"%s"}' % (row[0], row[1], row[2], row[3], row[4]))
        self.closeMysqlCur()
        self.msg = str({"messages": self.msg})
        self.sendMsg()

    def syncAllContacts(self):
        self.openMysqlCur()
        self.getDepartments()
        self.getJobs()
        self.getAllContacts()
        self.closeMysqlCur()
        self.msg = str({"departments": self.dictDep, "jobs": self.dictJob, "contacts": self.arrayContacts})
        # For test
        # print(self.msg)
        self.sendMsg()

    def syncAllGroups(self):
        self.openMysqlCur()
        stmt_select = "SELECT `gid`, `holder`, `name`, `member` FROM `group`"
        self.cur.execute(stmt_select)
        self.arrayGroup = []
        for row in self.cur.fetchall():
            self.arrayGroup.append({"gid": row[0], "holder": row[1], "name": row[2], "member": row[3]})
        self.closeMysqlCur()
        self.msg = str({"groups": self.arrayGroup})
        # for test
        # print(self.msg)
        self.sendMsg()

    def getDepartments(self):
        stmt_select = "SELECT `id`, `name` FROM `department` ORDER BY id"
        self.cur.execute(stmt_select)
        self.dictDep = {}
        for row in self.cur.fetchall():
            self.dictDep[row[0]] = row[1]
        return self.dictDep

    def getJobs(self):
        stmt_select = "SELECT `id`, `name` FROM `job` ORDER BY id"
        self.cur.execute(stmt_select)
        self.dictJob = {}
        for row in self.cur.fetchall():
            self.dictJob[row[0]] = row[1]
        return self.dictJob

    def getAllContacts(self):
        stmt_select = "SELECT `id`, `name`, `user`, `department`, `job`, `signing` FROM `user` WHERE `name`!=-1 ORDER BY id"
        # self.openMysqlCur()
        # stmt_select = "SELECT `id`, `name`, `user`, `department`, `job`, `signing` FROM `user` WHERE `name`<>'6YOR5oC7' ORDER BY id"
        self.cur.execute(stmt_select)
        self.arrayContacts = []
        for row in self.cur.fetchall():
            self.arrayContacts.append({"name": row[1], "user": row[2], "department": row[3], "job": row[4], "signing": row[5]})
        return self.arrayContacts

    def updateStatus(self):
        self.getMsg()
        self.openMysqlCur()
        stmt_update = "UPDATE user SET status=%d WHERE user=%s" % (self.msg["status"], self.msg["user"])
        self.cur.execute(stmt_update)
        self.closeMysqlCur()

    def updateSigning(self):
        self.getMsg()
        self.openMysqlCur()
        stmt_update = "UPDATE `user` SET `signing`='%s' WHERE `user`=%s" % (self.msg["signing"], self.msg["user"])
        self.cur.execute(stmt_update)
        self.closeMysqlCur()

    def createGroup(self):
        self.getMsg()
        self.openMysqlCur()
        stmt_insert = "INSERT INTO `group`( `holder`,`name`, `member`) VALUES('%s','%s', '%s')" % (self.msg["holder"], self.msg["name"], self.msg["member"])
        self.cur.execute(stmt_insert)
        stmt_select = "SELECT `gid` FROM `group` WHERE `holder`='%s' AND `name`='%s'" % (self.msg["holder"], self.msg["name"])
        self.cur.execute(stmt_select)
        self.groupGID = self.cur.fetchone()[0]
        self.closeMysqlCur()
        # TODO member alert
        # get group members array by gid
        self.groupMembers = self.msg["member"].split(',')
        self.group = self.msg
        self.dictContent = {
            "holder": self.group["holder"],
            "name": self.group["name"],
            "member": self.group["member"]
        }
        for member in self.groupMembers:
            self.msg = {
                "from": "0",
                "to": member,
                "type": 19,
                "content": str(base64.b64encode(bytes(str(self.dictContent), encoding="utf-8")), encoding="utf-8")
            }
            self.getTarPID()
            self.writeGroupMsg()
            if self.tarPID:
                try:
                    os.kill(self.tarPID, signal.SIGCHLD)
                except:
                    pass
            else:
                self.pushMsg()
                pass


if __name__ == '__main__':
    a = handleMessage(30666)
    # print(a.arrayContacts)
