#!/usr/bin/env python
#coding=utf-8

import tornado.web
import tornado.readdb as mrd

class userHandler(tornado.web.RequestHandler):
	def get(self):
		username=self.get_argument("user")
		user_infos=mrd.select_table=(table="users",column="*",condition="username",value=username)
		self.render("user.html",users=user_infos)
