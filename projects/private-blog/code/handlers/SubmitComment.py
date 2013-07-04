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
from MainPage import render_comment
del sys.path[0]


from AdminList import BlogAdmin

class SubmitComment(webapp.RequestHandler):
	def get(self):
		self.redirect('/error?reason=error')
		return
	def post(self):
		id_key = db.Key(self.request.get('commentupon'))
		if not id_key:
			self.redirect('/error?reason=error')
			return
		
		if self.request.get('edit')=='yes':
			comment=db.get(id_key)
			if not users.get_current_user() in ([comment.owner]+BlogAdmin):
				self.redirect("/error?reason=forbidden")
				return
			comment.body = self.request.get('commentbody')
			
		else:
			comment=BlogComment(body = self.request.get('commentbody'),refers_to = id_key,owner=users.get_current_user())
			#comment.body = self.request.get('body')
			#comment.refers_to = id_key
			#comment.owner=users.get_current_user()
			
		comment.put()
		
		if (self.request.get('jsactive')=='yes'):
			self.response.out.write(render_comment(comment))
			return
		else:
			self.redirect('/')
			return
