#!/usr/bin/env python 
# @Author:ZhangZhinan
# -*- coding:utf-8 -*-
import urllib.request
import re

def get_XiaoResponse(message):
    x = urllib.parse.quote(message)
    link = urllib.request.urlopen(
        "http://nlp.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%22sessionId%22%3A%22ff725c236e5245a3ac825b2dd88a7501%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A%227cd29df3450745fbbdcf1a462e6c58e6%22%2C%22body%22%3A%7B%22content%22%3A%22" + x + "%22%7D%2C%22type%22%3A%22txt%22%7D")
    html_doc = link.read().decode()
    reply_list = re.findall(r'\"content\":\"(.+?)\\r\\n\"', html_doc)
    response=("小i：" + reply_list[-1])
    return response

get_XiaoResponse('你好')