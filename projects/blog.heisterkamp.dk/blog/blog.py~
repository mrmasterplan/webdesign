#!/usr/bin/python

import time
import datetime
import _mysql
import snippets
from MySQLdb.constants import FIELD_TYPE

def dict_by_date(d1,d2):
  if(d1['date']>d2['date']):
    return -1
  if(d1['date']<d2['date']):
    return 1
  else:
    return 0


def main():
  db=_mysql.connect(host="localhost",user="simonhe",passwd="masterM",db="simonhe")
  db.query("""SELECT * FROM `blog_entries` WHERE 1""")
  r=db.store_result()
  rows=list( r.fetch_row(how=1,maxrows=0))
  rows.sort(dict_by_date)
  
  db.query("""SELECT * FROM blog_comments WHERE 1""" )
  r=db.store_result()
  comments=list(r.fetch_row(how=1,maxrows=0))
  
  
  for comment in comments:
    comment['text']=snippets.comment_open %(comment['entry'],comment['id'],comment['entry'],comment['id'])
    comment['text']+=snippets.comment_body%(comment['user'],comment['body'])
  #REMOVE predec attribute, do timestamp, go by lowest timestamp, submit without predec, java-live return with calculated predec

  now = int(time.mktime(datetime.datetime.now().timetuple()))

  def check_next(entry,parent,predec):
    foundcomment={}
    s=""
    for comment in comments:
      if(comment['entry']==entry and comment['parent']==parent and comment['predec']==predec):
        foundcomment=comment
    if not foundcomment:
      return s
    s+=foundcomment['text']
    s+=check_next(entry,foundcomment["id"],"0");
    s+=snippets.comment_close%(foundcomment['entry'],foundcomment['id'],now)
    s+=check_next(entry,parent,foundcomment['id']);
    return s


    
  for row in rows:
    row['comments']=snippets.comment_open %(row['id'],"0",row['id'],"0")
    row['comments']+=check_next(row['id'],"0","0")
    row['comments']+=snippets.comment_close%(row['id'],"0",now)
    
  #begin the output
  print snippets.head
  
  menu_entries = ""
  for row in rows:
    link_name = snippets.link_name % (row['date'],row['id'])
    print snippets.entry % (link_name,row['title'],row['date'],row['body'],
                            row['id'],row['id'],row['id'],row['comments'])
    menu_entries+=snippets.menu_entry % (link_name,row['date'])
    
  print snippets.end %(menu_entries)

