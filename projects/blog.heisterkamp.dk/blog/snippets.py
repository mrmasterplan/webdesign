#This file defines all snipets of html code that are used when creating the blog

head="""Content-type: text/html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">


<head>
<link rel="SHORTCUT ICON" href="favicon.ico">
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252" />
<title>My Blog (preliminary version)</title>

<link href="blog/blog.css" rel="stylesheet" type="text/css" />
<link href="blog/comment.css" rel="stylesheet" type="text/css" />
<link href="menu.css" rel="stylesheet" type="text/css" />
<link href="page.css" rel="stylesheet" type="text/css" />
<script src="jquery/jquery.js" txpe="text/javascript"></script>
<script src="blog/blog.js" txpe="text/javascript"></script>
</head>
<body>
<a name="top"></a>
<div id="page">
<div id="page_top"></div>
<div id="page_middle">
<div id="head_wrapper">
<div id="headsec"><h1 	align=center>SIMON's BLOG!</h1></div>
</div>
<div id="main_wrapper">
<div id="maintext">"""


comment_open="""<div class="comment comment-main-container" id="comment_%s_%s" entry_id="%s" comment_id="%s">
"""
comment_body="""<div class="comment-body">
<span class="commment-heading">
<span class="comment-user">%s</span> says:</span><br/>
<span class="comment-body">%s</span>
</div>
"""
comment_close="""<div class="comment-comment-container">
<div class="comment-link-container invisible"><a href="#" class="comment-link-comment">COMMENT</a>
</div>
<div class="comment-submit-container">
<form class="comment-submit-form" action="submit-comment.py" method="post">
User:<input name="comment-user" type="text"></input><input class="comment-submit-button" type="submit" value="submit"></input><br/>
<textarea name="comment-body" type="text" rows="3" cols="39"></textarea>
<input name="js_active" type="hidden" value="no"></input>
<input name="entry" type="hidden" value="%s"></input>
<input name="par-id" type="hidden" value="%s"></input>
<input name="timestamp" type="hidden" value="%s"></input>
</form>
</div>
</div>
</div>"""


link_name="Date_%s_%s"

entry="""
<div class="entry">
<div class="entry-body">
<a name="%s"><h3>%s, %s</h3></a>
<p>%s</p>
<a href="#top">Back to top.</a> <div class="rating" id="rate_%s" name="%s"></div>
<br/>
</div>
<div class="comment-section">
Comments:<br/>
<div class="entrycom" name="%s">
%s
</div>
</div>
</div>
<hr/>"""

menu_entry='<a class="menu"href="#%s">%s</a><br/>\n'

end="""
</div>

<div id="menu_spacer"></div>
<div id="menu_wrapper">
<div id="menu_top"></div><div id="menu_middle">
%s
<a href="enter-entry.php">New entry</a>
</div><div id="menu_bottom"></div></div>
</div>
<div id="botsec">
  <hr/>
  Menu, Copyright, and contact here.
</div>
</div> <!-- end page middle -->
<div id="page_bottom"></div>
</div><!-- end page -->
</body>
</html>
"""
