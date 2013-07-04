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
				
		console.log("commencing ajax send");
		$.ajax({
			type: "POST",
			url: "/submit-comment",
			data: {
				jsactive:"yes",
				commentbody:body,
				commentupon:key,
				},
			dataType: "html",
			success: function(res){
				console.log("ajax success executing");
				$(comment).children("div.comment-rest-container").append(res);
				charge_comment($(comment).children("div.comment-rest-container").children()[$(comment).children("div.comment-rest-container").children().length-1]);
			},
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
				
		console.log("commencing ajax send");
		$.ajax({
			type: "POST",
			url: "/submit-comment",
			data: {
				jsactive:"yes",
				commentbody:body,
				commentupon:key,
				edit:"yes",
				},
		});
		
		$(comment).children("div.comment-rest-container").children("div.comment-comment-container").children("div.comment_body").html("<pre>"+body+"</pre>")
		
		$(comment).children("div.comment-rest-container").children("div.comment-comment-container").find("a.comment-link-edit").click();
				
		$("textarea",this).attr("value","");
		return false;
	});
}
$(document).ready(function() {
	$("div.comment").each(function(i){
		charge_comment(this);
	});
	
	});
