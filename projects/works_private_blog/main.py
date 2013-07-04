#!/usr/bin/env python

import cgi,sys
import os
import datetime
import time
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


sys.path.insert(0,'code/handlers/')
from MainPage import *
from NewBlogEntry import NewBlogEntry
from SubmitComment import SubmitComment
from test_all_entries import TestHandler
from Error import ErrorHandler
from Remove import Remove
del sys.path[0]

from AdminList import BlogAdmin




application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/new-blog-entry', NewBlogEntry),
                                      ('/submit-comment', SubmitComment),
                                      ('/remove', Remove),
                                      ('/test',TestHandler),
                                      ('/error',ErrorHandler),
                                      ('/.*',ErrorHandler)
                                      ],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
