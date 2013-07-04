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
#from DataClasses import BlogEntry,BlogComment
del sys.path[0]


class MainPage(webapp.RequestHandler):
	def get_comments(self,refers_to):
		comment_query = db.GqlQuery('SELECT * FROM BlogComment WHERE refers_to = :parent ORDER BY date', parent=refers_to)
		comments=comment_query.fetch(1000)
		ret_string=""
		for comment in comments:
			ret_string+=render_comment(comment,self)
		return ret_string
	
	def get_entry(self,entry):
		entry.id_key=str(entry.key())
		entry.datelink = int(time.mktime(entry.date.timetuple()))
		
		entry.nicedate = entry.date.strftime("%a, %e %b %Y")
				
		values={
			'id_key':entry.id_key,
			'daughter_string':self.get_comments(entry.key()),
			}
		path = os.path.join(os.path.dirname(__file__), '../../htmls/comment_sec.html')
		entry.comments = template.render(path, values)
		
		values={'entry':entry,'isadmin':self.isadmin}
		
		path = os.path.join(os.path.dirname(__file__), '../../htmls/entry.html')
		return template.render(path, values)
	
	def get(self):
		reftime=datetime.datetime.now()
		self.call_user=users.get_current_user()
		self.isadmin=bool(self.call_user in BlogAdmin)
		
		blog_entry_query=db.GqlQuery("SELECT * FROM BlogEntry WHERE date >:1 ORDER BY date DESC",datetime.datetime(reftime.year-1,reftime.month,1))
		blogentries=blog_entry_query.fetch(10)
		
		menu_entries = []
		
		entries=""
		
		for entry in blogentries:
			entries += self.get_entry(entry)
			menu_entries.append({'link':int(time.mktime(entry.date.timetuple())),'title':entry.date.strftime("%d-%b-%Y")})	
			
				
					
		if self.call_user:
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Logout'
		else:
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Login'
			
				
		template_values = {
			'entries': entries,
			'isadmin':self.isadmin,
			'url': url,
			'url_linktext': url_linktext,
			'menu_entries': menu_entries,
			}
		path = os.path.join(os.path.dirname(__file__), '../../htmls/page_blog-main.html')
		self.response.out.write(template.render(path, template_values))

	
