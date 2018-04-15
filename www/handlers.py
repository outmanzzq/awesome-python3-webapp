#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: zzq
# 

import re, time, json, logging, hashlib, base64, asyncio

from coreweb import get, post

from models import User, Comment, Blog, next_id


@get('/')
async def index(request):
    users = await User.findAll()
    print(users)
    time.sleep(60)
    return {
        '__template__': 'test.html',
        'users': users
    }