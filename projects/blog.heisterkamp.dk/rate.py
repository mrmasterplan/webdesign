#!/usr/bin/python

import _mysql
import cgi
import cgitb; cgitb.enable()
from MySQLdb.constants import FIELD_TYPE

my_conv = {FIELD_TYPE.INT24: int}

db=_mysql.connect(host="localhost",user="simonhe",passwd="masterM",db="simonhe",conv=my_conv)

form = cgi.FieldStorage(keep_blank_values=1)

if (form.has_key('id') and form.has_key('rating')):
  id=form['id'].value
  rating=int(form['rating'].value)
  count=1
else:
  rating=0
  id=0
  count=0

db.query("""SELECT ratesum,ratecount FROM blog_entries WHERE id = %s"""%(id) )
r=db.store_result()
all_rows= r.fetch_row(how=1,maxrows=0)

newsum=rating +int(all_rows[0]['ratesum'])
newcount=count+int(all_rows[0]['ratecount'])

average = round((newsum / float(newcount)), 2);

print "Content-type: text/xml\n"
print "<ratings><average>%s</average><count>%s</count><id>%s</id></ratings>"%(average,newcount,id);

db.query("""UPDATE `blog_entries` SET ratesum=%s,ratecount=%s  WHERE id = %s"""%(newsum,newcount,id))
