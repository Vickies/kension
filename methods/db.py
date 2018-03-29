#!/usr/bin/env python
# coding=utf-8

import MySQLdb

conn=MySQLdb.connect(host="localhost",user="root",passwd="a110118",db="qiwsirtest",port=3307,charset="utf8") #connect sql

cur =conn.cursor()



