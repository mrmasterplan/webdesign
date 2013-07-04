#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#

import wsgiref.handlers


from google.appengine.ext import webapp


class MainHandler(webapp.RequestHandler):

  def get(self):
    f=open("plain.html")
    self.response.out.write(f.read())


def main():
  application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
