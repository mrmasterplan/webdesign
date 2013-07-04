import cgi,sys
import os
import datetime
import time
import logging
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

sys.path.insert(0,'code/')
from DataClasses import BlogEntry,BlogComment
import json
del sys.path[0]

sys.path.insert(0,'code/handlers/')
from MainPage import render_comment
del sys.path[0]

from AdminList import BlogAdmin

class UpdateComments(webapp.RequestHandler):
	def get(self):
		self.redirect('/error?reason=error')
		return
	def post(self):
		if not self.request.get('update')=='yes':
			self.redirect("/error?reason=forbidden")
			return
		update_since=datetime.datetime.now()-datetime.timedelta(0,30)
		comment_query=BlogComment.all().filter('date >',update_since).order('date')
		
		ret_list=[]
		for comment in comment_query:
			dict={"refers_to":str(comment.refers_to.key()),"body":render_comment(comment),"id":str(comment.key())}
			ret_list.append(dict)
		
		self.response.out.write(json.write(ret_list))
		return 
