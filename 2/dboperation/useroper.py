#!/usr/bin/env python
# coding: utf-8
import datetime

from config import settings


class UserInfoTableOperation:
    @staticmethod
    def checkuserlogin(self, username, password):
        s = settings.db.select('users', where='name=$username and password=$password', vars=locals())
        if not s:
            return False
        else:
            return True

    @staticmethod
    def reguserinfo(self, username, password, email):
        settings.db.insert('users', name=username, full_name=username, password=password,
                           login_count=1, last_login=1, email=email, admin=1, guest=1)

    @staticmethod
    def getuserid(self, username, password):
        s = settings.db.select('users', where='name=$username and password=$password', vars=locals())
        return s[0]


class TodoTableOperation:
    @staticmethod
    def get_by_id(self, todoid, userid):
        s = settings.db.select('todo', where='id=$todoid and userid=$userid', vars=locals())
        if not s:
            return False
        return s[0]

    @staticmethod
    def insert(self, title, userid, detail):
        settings.db.insert('todo', title=title, userid=userid, detail=detail, post_date=datetime.datetime.now())

    @staticmethod
    def updatefinish(self, finished, id, userid):
        settings.db.update('todo', finished=finished, where='id=$id and userid=$userid', vars=locals())

    @staticmethod
    def selectorder(self, userid):
        return settings.db.select('todo', where='userid=$userid', order='finished asc, id asc', vars=locals())

    @staticmethod
    def selectorderbyDetail(self, id):
        return settings.db.select('todo', where='id=$id', order='finished asc, id asc', vars=locals())

    @staticmethod
    def delete(self, id, userid):
        settings.db.delete('todo', where='id=$id and userid=$userid', vars=locals())

    @staticmethod
    def updatetitle(self, title, id, userid,content):
        settings.db.update('todo', title=title,detail=content, where='id=$id and userid=$userid', vars=locals())