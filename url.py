#!/usr/bin/env python
# coding=utf-8
"""
the url structure of website
"""
import sys #utf-8
reload(sys)
sys.setdefaultencoding("utf-8")

from handlers.index import IndexHandler

url=[
	(r"/",IndexHandler),
	(r"/user",UserHandler),
]
