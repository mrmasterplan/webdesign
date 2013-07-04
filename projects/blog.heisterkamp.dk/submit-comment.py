#!/usr/bin/python

cont_type_html="""Content-type: text/html

"""

html_escape_table = {"&": "&amp;",'"': "&quot;","'": "&apos;",">": "&gt;","<": "&lt;",}

def html_escape(text):
    """Produce entities within text."""
    L=[]
    for c in text:
        L.append(html_escape_table.get(c,c))
    return "".join(L)


import _mysql
import cgi
import cgitb; cgitb.enable()
from MySQLdb.constants import FIELD_TYPE
import time
import datetime
from blog import blog

#time.mktime(datetime.datetime.now().timetuple())
def main():
    now = int(time.mktime(datetime.datetime.now().timetuple()))
    
    db=_mysql.connect(host="localhost",user="simonhe",passwd="masterM",db="simonhe")
    form = cgi.FieldStorage()#keep_blank_values=1)
    
    if not(form.has_key('js_active') 
           and form.has_key('comment-user')
           and form.has_key('comment-body')
           and form.has_key('entry')
           and form.has_key('timestamp')
           and form.has_key('par-id')):
        blog.main()
        return

    comment_user = html_escape(form['comment-user'].value)[:20]
    comment_body = html_escape(form['comment-body'].value)[:200]
    par_id       = int(form['par-id'].value)
    timestamp    = int(form['timestamp'].value)
    entry        = int(form['entry'].value)

    db.query("""SELECT * FROM blog_comments WHERE entry="%s" AND parent="%s" AND user="%s" AND body="%s" AND timestamp="%s" """ %(entry,par_id,comment_user,comment_body,timestamp))
    r=db.store_result()
    if not r.num_rows()==0:
        blog.main()
        return

    db.query("""INSERT INTO blog_comments (entry,parent,timestamp,user,body) VALUES ('%s','%s',%s,'%s','%s')""" % (entry,par_id,timestamp,comment_user,comment_body))
    db.query("""SELECT id FROM blog_comments WHERE entry="%s" AND parent="%s" AND user="%s" AND body="%s" AND timestamp="%s" """ %(entry,par_id,comment_user,comment_body,timestamp))
    r=db.store_result()
    rows=list(r.fetch_row(how=1,maxrows=0))
    id=int(rows[0]['id'])

    if not form['js_active'].value=='yes':
        blog.main()
        return
    else:
        print cont_type_html
        print blog.snippets.comment_open %(entry,id,entry,id)
        print blog.snippets.comment_body%(comment_user,comment_body)
        print blog.snippets.comment_close%(entry,id,now)
        return

main() 
