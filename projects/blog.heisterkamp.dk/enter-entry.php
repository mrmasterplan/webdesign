<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">


<head>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252" />
<title>My Blog (New Entry Submit)</title>

<link href="submit.css" rel="stylesheet" type="text/css" />
<link href="page.css" rel="stylesheet" type="text/css" />



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
<div id="submit-form">
<form name="new_entry" action="submit-entry.py" method="POST">
Submit new entry:<br/>
Title:<input name="title" type="text"><br/>
Date:<input name="date" type="text" value=<?php echo '"'.date("Y-m-d").'"' ?> ><br/>
<textarea name="body" type="text" rows="25" cols="70" ></textarea><br/>
Submit pass:<input name="pwd" type="password"><br/>
<input type="submit" value="Go post it">
</form>
</div>
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
