
$(document).ready(function(){
	//alert("i made it dinghey");
	var myJSON = "";
       



//	$('input#submit.btn.btn-default').click(function(){
	//alert('made it here');
	$('#loader').show();	 
	var question;
	  
	 $.ajax({
		
		url: "/_askChatBot/<id>",
		data: {param: question},
		type: "POST",
		success: function(response) {
			console.log(response);
			//$('#ChatBotResponsesLog').append(response);

			console.log('Going to fetch a reply from diskey-bot. please hold while the dingo connects with you');
			 			
			//run_chat_bot_model();
		},
		error: function(err) {
			console.log(err);		
		}
	 });	
	}); 

	 

	function run_chat_bot_model(){
		console.log("Connecting to Chat Bot");
		var question;		
		$.ajax({
		
		url: "/_fetchFromChatBot/<id>",
		data: {param: question},
		type: "POST",
		success: function(response) {
			$('#loader').hide();
			console.log(response);
			$('#ChatBotResponses').append(response + "<br/>");
			

			console.log('A new response has been loaded from the chat bot model!');
			
		},
		error: function(err) {
			console.log(err);		
		}
	 });
	}

	 
	


	$('#ClearChatBot').click(function(){
		$('#ChatBotResponses').empty();
	});


	

