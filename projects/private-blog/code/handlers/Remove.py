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
del sys.path[0]

sys.path.insert(0,'code/handlers/')
from MainPage import *
del sys.path[0]


from AdminList import BlogAdmin

class Remove(webapp.RequestHandler):
	def remove_daughters(self, id):
		comment_query = db.GqlQuery('SELECT * FROM BlogComment WHERE refers_to = :parent', parent=id)
		
		for comment in comment_query:
			self.remove_daughters(comment.key())
			db.delete(comment)
		return
		
	def get(self):
		id=db.Key(self.request.get('id'))
		if not id:
			self.redirect('/error?reason=error')
			return

		allowed= (users.get_current_user() in BlogAdmin)
	
		if not allowed:
			self.redirect('/error?reason=forbidden')
			return
		if not self.request.get('confirm')=='yes':
			object_to_remove=""
			main=MainPage()
			main.isadmin=False
			main.call_user=0
			object=db.get(id)
			if id.kind()=='BlogEntry':
				object_to_remove=main.get_entry(object)
			elif id.kind()=='BlogComment':
				object_to_remove=render_comment(object,main)
				
			values={
				'target':object_to_remove,
				'id':str(object.key())
				}
			path = os.path.join(os.path.dirname(__file__), '../../htmls/page_remove.html')
			self.response.out.write(template.render(path, values))
		else:
			self.remove_daughters(id)
			db.delete(db.get(id))
			self.redirect('/')
			
		
	def post(self):
		self.redirect('/error?reason=error')
		return
		
