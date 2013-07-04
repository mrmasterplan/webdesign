import cgi
import os
import datetime
import time
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from AdminList import BlogAdmin

class ErrorHandler(webapp.RequestHandler):
	def get(self):
		reason=self.request.get('reason')
		
		path = os.path.join(os.path.dirname(__file__), '../../htmls/page_error.html')
		self.response.out.write(template.render(path,{'reason':reason}))
		return
