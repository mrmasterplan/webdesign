//Start comment injection
function insertcomment(id,entry,parent,user,comment){
    var par_id ="#comment_"+entry+"_"+parent;
    $(par_id).append("<div class=\"comment\" id=\"comment_"+entry+"_"+id+"\"><b>"+user+"</b> says:<br/>"+comment+"</div>");
    // alert("Insert something into "+par_id);
}

function checknext(entry,parent,predec){
    if ( !(entry==="") && !(parent==="")&& !(predec==="")){
    $.get("getcomment.py",{entry:entry,parent:parent,predec:predec},function(xml){
	    if ($("all",xml).text()!=""){
		insertcomment($("id",xml).text(),entry,parent,$("user",xml).text(),$("body",xml).text());
		checknext(entry,$("id",xml).text(),0);
		checknext(entry,parent,$("id",xml).text());
	    }
	});}
}

$(document).ready(function() {
	//Start loading the comments
	$("div.entrycom").each(function(i){checknext($(this).attr("name"),0,0)});
	  
    });