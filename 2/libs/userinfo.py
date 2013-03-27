#!/usr/bin/env python
# coding: utf-8

from lxml import etree


class User:
    @staticmethod
    def returnuserinfo(data):
        root = etree.fromstring(data)
        child = list(root)
        tmplist = {}
        for i in child:
            tmplist[i.tag] = i.text
        return tmplist


class UserMessage:
    @staticmethod
    def returntxtMessage( FromUserName, ToUserName, CreateTime, MsgType, Content):
        template = """<xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[%s]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                    <FuncFlag>0</FuncFlag>
                    </xml>"""
        values = template % (FromUserName, ToUserName, CreateTime, MsgType, Content)
        return values


