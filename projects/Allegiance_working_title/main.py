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


application = webapp.WSGIApplication(
                                     [('/', MainPage)
                                       ],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
