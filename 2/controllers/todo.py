#!/usr/bin/env python
# coding: utf-8

import hashlib

import web
from libs import userinfo
from config.settings import config
import datetime
import time
from config import settings


class LogTableOperation:
    @staticmethod
    def InsertLog(log, datetime):
        settings.db.insert('logs', log=log, datetime=datetime)


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
        #接收微信的请求内容
        data = web.data()
        #解析XML内容,返回列表
        recv = userinfo.User.returnuserinfo(data)
        #测试demo 所以接收到啥内容，就原样返回
        #文本模板
        if recv['MsgType'] == 'text':
            #格式化文本消息
            echostr = userinfo.UserMessage.returntxtMessage(recv['FromUserName'], recv['ToUserName'],
                                                            recv['CreateTime'],
                                                            recv['MsgType'], recv['Content'])
            #插入日志调试
            LogTableOperation.InsertLog(echostr,
                                        time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time())))


            #图片模板
        if recv['MsgType'] == 'image':
            textTpl = """
            <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[%s]]></MsgType>
                <Content><![CDATA[%s]]></Content>
                <FuncFlag>0</FuncFlag>
            </xml>"""
            echostr = textTpl % (
                recv['FromUserName'], recv['ToUserName'], recv['CreateTime'], "text", recv['PicUrl'])
        if recv['MsgType'] == 'location':
            textTpl = """
            <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[%s]]></MsgType>
                <Content><![CDATA[%s]]></Content>
                <FuncFlag>0</FuncFlag>
            </xml>"""
            content = "您的地理位置为X:" + str(recv['Location_X']) + "Y:" + str(recv['Location_Y'])
            echostr = textTpl % (
                recv['FromUserName'], recv['ToUserName'], recv['CreateTime'], "text", content)
        if recv['MsgType'] == 'link':
            textTpl = """
            <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[%s]]></MsgType>
                <Content><![CDATA[%s]]></Content>
                <FuncFlag>0</FuncFlag>
            </xml>"""
            echostr = textTpl % (
                recv['FromUserName'], recv['ToUserName'], recv['CreateTime'], "text", str(recv['Url']))
        return echostr




