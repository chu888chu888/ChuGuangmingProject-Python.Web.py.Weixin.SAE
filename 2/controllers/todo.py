#!/usr/bin/env python
# coding: utf-8

import hashlib
from lxml import etree

import web

from config.settings import config


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

        #测试demo 所以接收到啥内容，就原样返回
        #文本模板
        if recv['MsgType'] == 'text':
            textTpl = """<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[%s]]></MsgType>
                <Content><![CDATA[%s]]></Content>
                <FuncFlag>0</FuncFlag>
                </xml>"""
            echostr = textTpl % (
                recv['FromUserName'], recv['ToUserName'], recv['CreateTime'], recv['MsgType'], recv['Content'])
            #图片模板
        if recv['MsgType'] == 'image':
            imgTpl = """
            <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[%s]]></MsgType>
                <Content><![CDATA[%s]]></Content>
                <FuncFlag>0</FuncFlag>
            </xml>"""
            echostr = imgTpl % (
                recv['FromUserName'], recv['ToUserName'], recv['CreateTime'], "text", recv['PicUrl'])
        if recv['MsgType'] == 'location':
            imgTpl = """
            <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[%s]]></MsgType>
                <Content><![CDATA[%s]]></Content>
                <FuncFlag>0</FuncFlag>
            </xml>"""
            echostr = imgTpl % (
                recv['FromUserName'], recv['ToUserName'], recv['CreateTime'], "text", str(recv['Label']))
        if recv['MsgType'] == 'link':
            imgTpl = """
            <xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[%s]]></MsgType>
                <Content><![CDATA[%s]]></Content>
                <FuncFlag>0</FuncFlag>
            </xml>"""
            echostr = imgTpl % (
                recv['FromUserName'], recv['ToUserName'], recv['CreateTime'], "text", str(recv['Url']))
        return echostr




