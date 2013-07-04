import cgi,sys
import os
import datetime
import time
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

sys.path.insert(0,'code/')
from DataClasses import BlogEntry,BlogComment
del sys.path[0]


from AdminList import BlogAdmin

class NewBlogEntry(webapp.RequestHandler):
	def get(self):
		if not users.get_current_user() in BlogAdmin:
			self.redirect('/error?reason=forbidden')
			return
      
		title=""
		entrykey=""
		body=""

		if self.request.get('update'):
			entrykey=self.request.get('update')
			entry=db.get(entrykey)
			title=entry.title
			body=entry.body

		template_values={
			'title':title,
			'entrykey':entrykey,
			'body':body,
			}
		path = os.path.join(os.path.dirname(__file__), '../../htmls/page_submit-entry.html')
		self.response.out.write(template.render(path, template_values))

	def post(self):
		if not users.get_current_user() in BlogAdmin:
			self.redirect('/error?reason=forbidden')
			return

		if self.request.get('entry_key'):
			entry=db.get( self.request.get('entry_key'))
		else:
			entry = BlogEntry()
		    
		entry.title = self.request.get('title')
		entry.body = self.request.get('body')
		
		entry.ratesum=0
		entry.ratecount=0

		entry.put()

		self.redirect('/')
