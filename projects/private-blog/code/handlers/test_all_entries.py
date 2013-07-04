#import cgi
import os,sys
#import datetime
#import time
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
#from google.appengine.ext.webapp.util import run_wsgi_app

sys.path.insert(0,'code/')
from DataClasses import BlogEntry,BlogComment
del sys.path[0]

from AdminList import BlogAdmin

class TestHandler(webapp.RequestHandler):
	def get(self):
		if not users.get_current_user() in BlogAdmin:
			self.redirect('/error?reason=forbidden')
			return
			
		comment_query = BlogComment.all()
		
		retstring = ""
		for comment in comment_query:
			retstring += "\nrefers_to= "+str(comment.refers_to)
			retstring += "\nowner    = "+str(comment.owner.nickname())
			retstring += "\nbody     = "+comment.body
			retstring += "\ndate     = "+str(comment.date)
			retstring += "\n"
			
		path = os.path.join(os.path.dirname(__file__), '../../htmls/page_blank.html')
		self.response.out.write(template.render(path,{'all':retstring,}))
