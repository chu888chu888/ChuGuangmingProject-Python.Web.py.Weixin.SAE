#!/usr/bin/env python
# coding: utf-8

import hashlib
from lxml import etree
import time

import web

from config.settings import config, textMessage
from config import settings


class LogTableOperation:
    @staticmethod
    def InsertLog(log, datetime):
        settings.db.insert('logs', log=log, datetime=datetime)


class TextMessageTableOperation:
    @staticmethod
    def InsertTextMessage(fromuser, touser, datetime, content):
        settings.db.insert('textmessage', fromuser=fromuser, touser=touser, datetime=datetime, content=content)


class weixin:
    #GET方法，主要用来注册url
    def GET(self):
        data = web.input()
        #以下是微信公众平台请求的参数
        #微信加密签名
        signature = data.signature
        #时间戳
        timestamp = data.timestamp
        #随机数
        nonce = data.nonce
        #随机字符串
        echostr = data.echostr

        #自己定义的 TOKEN
        token = config['TOKEN']

        #对微信发送的请求，做验证
        tmplist = [token, timestamp, nonce]
        tmplist.sort()
        tmpstr = ''.join(tmplist)
        hashstr = hashlib.sha1(tmpstr).hexdigest()

        #如果相等，返回验证信息
        if hashstr == signature:
            return echostr

        #如果不相等，返回错误，并打印调试信息
        print signature, timestamp, nonce
        print tmpstr, hashstr
        return 'Error' + echostr


    def POST(self):
        #有以下几种类型
        #文本 值为：text
        #图片 值为：image
        #地理信息 值为：location
        #连接信息 值为：link
        #接收微信的请求内容
        data = web.data()
        #解析XML内容
        root = etree.fromstring(data)
        child = list(root)
        recv = {}
        for i in child:
            recv[i.tag] = i.text

        #print data
        #print recv
        '''
        imgTpl = textMessage
        echostr = imgTpl % (
            'oZfN9jgzVGy0hckH4uIGCCEF2NAE','gh_41d883ddb465', '1364371886', "text", '这是定时的测试功能')
        return echostr
        '''
        #测试demo 所以接收到啥内容，就原样返回
        #发送的是文本信息
        if recv['MsgType'] == 'text':
            textTpl = textMessage
            echostr = textTpl % (
                recv['FromUserName'], recv['ToUserName'], recv['CreateTime'], recv['MsgType'], "谢谢您的发送，我会第一时间联系您！")
            #插入用户发送消息的内容到textmessage
            TextMessageTableOperation.InsertTextMessage(recv['FromUserName'], recv['ToUserName'],
                                                        time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time())),
                                                        recv['Content'])
            #发送的是图片信息
        if recv['MsgType'] == 'image':
            imgTpl = textMessage
            echostr = imgTpl % (
                recv['FromUserName'], recv['ToUserName'], recv['CreateTime'], "text", recv['PicUrl'])
            #发送的是地理信息
        if recv['MsgType'] == 'location':
            imgTpl = textMessage
            echostr = imgTpl % (
                recv['FromUserName'], recv['ToUserName'], recv['CreateTime'], "text", str(recv['Location_X']))
            #发送的是连接信息
        if recv['MsgType'] == 'link':
            imgTpl = textMessage
            echostr = imgTpl % (
                recv['FromUserName'], recv['ToUserName'], recv['CreateTime'], "text", str(recv['Url']))
        return echostr





