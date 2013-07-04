#!/usr/bin/python

import _mysql
import cgi
import cgitb; cgitb.enable()
from MySQLdb.constants import FIELD_TYPE

my_conv = {FIELD_TYPE.INT24: int}

db=_mysql.connect(host="localhost",user="simonhe",passwd="masterM",db="simonhe",conv=my_conv)

form = cgi.FieldStorage()

if not (form.has_key('entry') and form.has_key('parent') and form.has_key('predec')):
    print "Content-type: text/xml\n"
    print "<all></all>"
else:
    #  id=int(form.getlist('id')[0])
    entry=int(form.getvalue('entry'))
    parent=int(form.getvalue('parent'))
    predec=int(form.getvalue('predec'))
    #  user=cgi.escape(form.getlist('user')[0]).replace("\'","\\'")
    #  comment=cgi.escape(form.getlist('comment')[0]).replace("\'","\\'")
    
    db.query("""SELECT id,user,comment FROM blog_comments WHERE entry = %s AND parent = %s AND predec = %s"""%(entry,parent,predec) )
    r=db.store_result()
    all_rows= r.fetch_row(how=1,maxrows=0)
    
    print "Content-type: text/xml\n"
    if (len(all_rows)!=0):
        print '<?xml version="1.0" encoding="UTF-8"?>'
        print "<all>"
        
        for row in all_rows:
            print """<comment><id>%s</id><user>%s</user><body>%s</body></comment>"""%(row['id'],row['user'],row['comment'])
            
        print "</all>"
    else:
        print "<all></all>"

