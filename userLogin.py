#!/usr/bin/env python3.4

import handleMessage

class userLogin(object):
  """docstring for ClassName"""
  def __init__(self):
    pass    
  def __call__(self):
    getMsg=handleMessage()
    msg=getMsg.getMessage()
    if self.checkAccount(msg["user"], msg["password"]):
      self.loginSuccess(msg["user"])
      return
    else:
      self.loginFail()
      return
  def loginSuccess(self,user):
    #TODO
    pass
  def loginFail(self):
    #TODO
    pass
  def checkAccount(self, user, password):
    #TODO
    return 1

if __name__ == '__main__':
  l=userLogin()
  l()