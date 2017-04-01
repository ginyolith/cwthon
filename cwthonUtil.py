# -*- coding: utf-8 -*-
from types import *

def getStr(target):
    targetType = type(target)
    if targetType is UnicodeType:
        return target.encode('utf-8')
    elif targetType is StringType:
        return target
    elif targetType is IntType:
        return str(target)

def listToDict(list, keyColumn):
    parsed = dict()
    for item in list :
        key = item.get(keyColumn)
        parsed.update({key : item})

    return parsed

def replaceParam(target, params):
    for key in params.keys() :
        value = params[key]
        replaceKey = '{' + key +'}'
        if value and replaceKey:
            target = target.replace(replaceKey, str(value))
            #target = target.translate(str.maketrans(replaceKey, str(value)))
    return target
