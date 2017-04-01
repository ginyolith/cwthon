# -*- coding: utf-8 -*-
import logging
import requests
import json
import cwthonBase
import cwthonUtil
from cwthonProp import *
from types import *

contactList = cwthonBase.updateCountctListCache()
roomList = cwthonBase.updateRoomListCache()

def getContactInfo(account_id):
    contactInfo = contactList.get(account_id)
    if contactInfo is None :
        contactList.update(cwthonBase.updateCountctListCache())
        contactInfo = contactList.get(account_id)
    return contactInfo;

def getRoomInfo(room_id) :
    roomInfo = roomList.get(room_id)
    if roomInfo is None :
        roomList.update(cwthonBase.updateRoomListCache())
        roomInfo = roomList.get(room_id)
    return roomInfo;

class cwReq:
    __endPoint = None
    __params = None
    def sendMsgToAccount(self, account_id, msg):
        self.__endPoint = cwEndPoint.SEND_MSG
        self.__params = getContactInfo(account_id)
        self.__params.update({'body' : msg})
        self.__send()

    def sendMsgToRoom(self, room_id, msg):
        self.__endPoint = cwEndPoint.SEND_MSG
        self.__params = getRoomInfo(room_id)
        self.__params.update({'body' : msg})
        self.__send()

    def __send(self):
        method = self.__endPoint.value['method']
        if method is None :
            logging.error("cwReq cant send. method was None")
            return

        endPointUrl = self.__getEndPointUrl()

        res = None

        if method is reqMethods.POST:
            res = requests.post(
                url=endPointUrl,
                headers=cwthonBase.reqHdr,
                data={'body' : self.__params['body']}
                )
        elif method is reqMethods.GET:
            logging.error('send GET req Not implemented')
        elif method is reqMethods.DELETE:
            logging.error('send DELTE req is Not implemented')

        return cwRes(res)

    def __getEndPointUrl(self):
        path = cwthonUtil.replaceParam(
            target = self.__endPoint.value['url'],
            params = self.__params)
        return cwthonBase.baseUrl + path
    
class cwRes:
    def __init__(self, res):
        self.__res = res
