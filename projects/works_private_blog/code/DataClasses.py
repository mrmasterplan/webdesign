import cgi
import os
import datetime
import time
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class BlogEntry(db.Model):
  date = db.DateTimeProperty(auto_now_add=True)
  title = db.StringProperty()
  body = db.TextProperty()
  ratesum = db.IntegerProperty()
  ratecount = db.IntegerProperty()
# Idea behing comment ordering is this
# The comments are in sequence as they are displayed.
# A new comment will be inserted by Parent id
# The parents immediate daughters will have to be waled through
# until the end of the coment tree is found.
# This way submitting is intensive, reading is easy as pie

class BlogComment(db.Model):
  refers_to = db.ReferenceProperty()
  date = db.DateTimeProperty(auto_now_add=True)
  owner = db.UserProperty()
  body = db.TextProperty()
