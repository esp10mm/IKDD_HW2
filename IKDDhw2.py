#!/usr/bin/env python
#coding:utf-8

import sys
from modules.iServDB import iServDB

class result:
    def __init__(self, text, user, uid):
        self.text = text
        self.user = user
        self.uid = uid

db = iServDB('patrick5267_db_8874','patrick5267_user_8874','dXYMWPeJ')
doc = db.query('SELECT * FROM "twitter" WHERE q = \'%s\''% (sys.argv[1]))

results = []

for data in doc:
    results.append(result(data[1], data[2], data[3]))

results.sort(key=lambda result: result.uid)

for result in results:
    print '--------------------text---------------------'
    print result.text
    print '-----------------user_name-------------------'
    print result.user
    print '------------------user_id--------------------'
    print result.uid + '\n'
