var update_interval=30;

function charge_comment(comment){
	$(comment).children("div.comment-rest-container").children("div.comment-comment-container").children("div.comment-submit-container").addClass("invisible")
	$(comment).children("div.comment-rest-container").children("div.comment-comment-container").children("div.comment-link-container").removeClass("invisible").find("a").removeClass("invisible");
	$(comment).children("div.comment-rest-container").children("div.comment-comment-container").each(function(i){
		var container = this;
		$(this).find("a.comment-link-comment").click(function(e){
			e.preventDefault();
			$(container).find("div.comment-edit-container").addClass("invisible");
			$(container).find("div.comment-submit-container").toggleClass("invisible");
			$(container).find("div.comment_body").removeClass("invisible");
			if (!($(container).find("div.comment-submit-container").hasClass("invisible"))){
				$(container).find("div.comment-submit-container").find("textarea").focus();
			}
		});
		$(this).find("a.comment-link-edit").click(function(e){
			e.preventDefault();
			$(container).find("div.comment-submit-container").addClass("invisible");
			$(container).find("div.comment_body").toggleClass("invisible");
			$(container).find("div.comment-edit-container").toggleClass("invisible");
			if (!($(container).find("div.comment-edit-container").hasClass("invisible"))){
				$(container).find("div.comment-edit-container").find("textarea").focus();
			}
		});
	});
	
	$(comment).children("div.comment-rest-container").children("div.comment-comment-container").children("div.comment-submit-container").children("form.comment-submit-form").submit(function(){
		var body=$("textarea",this).val()
		var key=$("input[name='commentupon']",this).val()
		var form= this
		
		if(body.length > 200){
			alert("Body must contain less than 200 characters.");
			return false;
		}
		
		$.ajax({
			type:"POST",
			url:"/submit-comment",
			data:{
				jsactive:"yes",
				commentbody:body,
				commentupon:key
			},
			dataType:"html",
			success: function(res){
				$(comment).children("div.comment-rest-container").append(res);
				charge_comment($(comment).children("div.comment-rest-container").children()[$(comment).children("div.comment-rest-container").children().length-1]);
			}
		});
		
		$(comment).children("div.comment-rest-container").children("div.comment-comment-container").find("a.comment-link-comment").click();
				
		$("textarea",this).attr("value","");
		return false;
	});
			
	$(comment).children("div.comment-rest-container").children("div.comment-comment-container").children("div.comment-edit-container").children("form.comment-edit-form").submit(function(){
		var body=$("textarea",this).val()
		var key=$("input[name='commentupon']",this).val()
		var form= this
		
		if(body.length > 200){
			alert("Body must contain less than 200 characters.");
			return false;
		}
		
		$.ajax({
			type:"POST",
			url:"/submit-comment",
			data:{
				jsactive:"yes",
				commentbody:body,
				commentupon:key,
				edit:"yes"
				}
		});
		
		$(comment).children("div.comment-rest-container").children("div.comment-comment-container").children("div.comment_body").html("<pre>"+body+"</pre>")
		
		$(comment).children("div.comment-rest-container").children("div.comment-comment-container").find("a.comment-link-edit").click();
				
		$("textarea",this).attr("value","");
		return false;
	});
}

function update(){
	$.ajax({
		type:"POST",
		url:"/update-comments",
		data:{update:'yes'},
		dataType:"json",
		success:function(json){
			for(i=0;i<json.length;i++){
				if($("#"+json[i].id).length==0){
					$("#"+json[i].refers_to).children("div.comment-rest-container").append(json[i].body);
					$("#"+json[i].id).each(function(j){charge_comment(this)});
				}
			}
		}
	});
}

var int;

function LoadFnObj(){
	this.funcs = new Array();
}
LoadFnObj.prototype.add = function(f){
	this.funcs[this.funcs.length] = f;
}
LoadFnObj.prototype.execute = function(){
	for( var i = 0; i < this.funcs.length; i++ ){
		this.funcs[i](); // Call the function
	}
}

var loadfns = new LoadFnObj();


function menu_pretty() {
	//Prettify the menu
	$("#menu_wrapper").css("border","none");
	$("#menu_wrapper").css("padding","0px");

	var tags =["tl","tr","bl","br"];
	for (var i=0;i<tags.length;++i){
		var name ="#menu_corner_"+tags[i];
		$(name).css("background","url(/images/menu_corner_"+tags[i]+".png)");
		$(name).css("width","22px");
		$(name).css("height","22px");
	}

	$("#menu_top").css("background","url(/images/menu_t.png) repeat-x");
	$("#menu_top").css("height","22px");

	$("#menu_middle").css("background","url(/images/menu_150_center.png) repeat-y");
	
	$("#menu_body").css("background","url(/images/menu_l.png) repeat-y");
	$("#menu_body").css("padding-left","15px");
	$("#menu_body").css("padding-right","5px");
	
	$("#menu_r").css("background","url(/images/menu_r.png) repeat-y");
	$("#menu_r").css("width","10px");
	$("#menu_r").css("height",$("#menu_body").height()+"px");
	
	$("#menu_bottom").css("background","url(/images/menu_b.png)");
	$("#menu_bottom").css("height","22px");
	
	$("#menu_wrapper").css("width",$("#menu_body").width()+30);
}

loadfns.add(menu_pretty);

$(document).ready(function() {
	$("div.comment").each(function(i){charge_comment(this);});
	
	int=setInterval("update()",30000);

	loadfns.execute();
});
