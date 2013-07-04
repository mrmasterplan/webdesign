#!/usr/bin/python

import _mysql
import cgi
#import cgitb; cgitb.enable()
from MySQLdb.constants import FIELD_TYPE

my_conv = {FIELD_TYPE.INT24: int}

db=_mysql.connect(host="localhost",user="simonhe",passwd="masterM",db="simonhe",conv=my_conv)
#db.query("""SELECT * FROM `blog_entries` WHERE 1""")
#r=db.store_result()
#all_rows= r.fetch_row(how=1,maxrows=0)

print "Content-type: text/html\n"

f = open('submit-entry/head','r')
print f.read()
f.close()

form = cgi.FieldStorage(keep_blank_values=1)

if not (form.has_key('title') and form.has_key('date') and form.has_key('body') and form.has_key('pwd')):
  print "One of the fields is missing."
else:
  if not (form['pwd'].value=="godoit"):
    print "Wrong password."
  else:
    print "\n<h3>%s, %s</h3>\n<p>" % (form['title'].value,form['date'].value)
    BODY =form['body'].value
    BODY=BODY.replace("\'","\\'")
    print BODY
    print "</p>"
    db.query("""INSERT INTO blog_entries (date,title,body) VALUES ('%s','%s','%s')""" % (form['date'].value,form['title'].value,BODY))
    print "<p>Your entry has been submitted</p>\n<a href=\"index.py\">Return to blog</a>" 



f = open('submit-entry/end','r')
print f.read()
f.close()

