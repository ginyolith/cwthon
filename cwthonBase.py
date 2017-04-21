# -*- coding: utf-8 -*-
import logging
import requests
import json
import cwthonUtil
from types import *
from xml.etree import ElementTree
import os

baseUrl = "https://api.chatwork.com/v2/"
reqHdr = {'X-ChatWorkToken': os.getenv('CW_TOKEN', "")}

def updateCountctListCache():
    apiUrl = baseUrl + 'contacts'
    res = requests.get(url=apiUrl, headers=reqHdr)
    beforeParse = json.loads(res.text)
    return cwthonUtil.listToDict(beforeParse, keyColumn='account_id')

def updateRoomListCache():
    apiUrl = baseUrl + 'rooms'
    res = requests.get(url=apiUrl, headers=reqHdr)
    beforeParse = json.loads(res.text)
    return cwthonUtil.listToDict(beforeParse, keyColumn='room_id')
