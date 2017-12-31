
$(document).ready(function(){
	//alert("i made it dinghey");
	var myJSON = "";
       


/*
	$('input#submit.btn.btn-default').click(function(){
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
	});  */

	$('#AskChatBotRandom').click(function(){
	 var questionRandom;
	 $('#loader').show(); 
	 $.ajax({
		
		url: "/_askChatBotRandom/<id>",
		data: {param: questionRandom},
		type: "POST",
		success: function(response) {
			console.log(response);
			//$('#ChatBotResponsesLog').append(response);
			

			console.log('Going to fetch a random reply from diskey-bot. please hold while the dingo connects with you');
			 			
			run_chat_bot_modelRandom();
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

	function run_chat_bot_modelRandom(){
		console.log("Connecting to Chat Bot");
		var questionRandom;		
		$.ajax({
		
		url: "/_fetchFromChatBotRandom/<id>",
		data: {param: questionRandom},
		type: "POST",
		success: function(responseRandom) {
			$('#loader').hide();
			console.log(responseRandom);
			$('#ChatBotResponses').append(responseRandom + "<br/>");
			

			console.log('A new random response has been loaded from the chat bot model!');
			
		},
		error: function(err) {
			console.log(err);		
		}
	 });
	}

	


	$('#ClearChatBot').click(function(){
		$('#ChatBotResponses').empty();
	});





	 $('#GetMessage').click(function(){
	 var consumer;
	 $.ajax({
		
		url: "/_getMessage",
		data: {param: consumer},
		type: "POST",
		success: function(response) {
			console.log(response);
			$('#ShowKafkaMessagefromGetter').append(response);
		},
		error: function(err) {
			console.log(err);		
		}
	 });	
	});       


	$('#StartKafkaProducer').click(function(){
	 var producer = "sometext";
	 $.ajax({
		
		url: "/_StartKafkaProducer",
		data: {param: producer},
		type: "POST",
		success: function(response) {
			console.log(response);
			$('#ShowKafkaProducerDetails').append(response);
		},
		error: function(err) {
			console.log(err);		
		}
	 });	
	});	

	$('#StartKafkaConsumer').click(function(){
	 var topic = "cryBert";
	 var messages = "sometextmessage";
	 var numberOfMessages = 0;
	var consumer;
	 $.ajax({
		
		url: "/_StartKafkaConsumer",
		data: {param: consumer},
		type: "POST",
		success: function(response) {
			console.log(response);
			
			$('#ShowKafkaConsumerDetails').append(response);
		},
		error: function(err) {
			console.log(err);		
		}
	 });	
	});

	
	$('#SendKafkaMessage').click(function(){
	 var sendProducerMsg = "sometext";
	 $.ajax({
		
		url: "/_SendKafkaMessage",
		data: {param: sendProducerMsg},
		type: "POST",
		success: function(response) {
			console.log(response);
			$('#ShowKafkaMessage').append(response);
		},
		error: function(err) {
			console.log(err);		
		}
	 });	
	});

	$('#StopKafkaConsumer').click(function(){
	 var topic = "cryBert";
	 $.ajax({
		
		url: "/_StopKafkaConsumer",
		data: {param: topic},
		type: "POST",
		success: function(response) {
			console.log(response);
			$('#ShowKafkaStopConsumerDetails').append(response);
		},
		error: function(err) {
			console.log(err);		
		}
	 });	
	});

	$('#StopKafkaProducer').click(function(){
	 var topic = "cryBert";
	 $.ajax({
		
		url: "/_StopKafkaProducer",
		data: {param: topic},
		type: "POST",
		success: function(response) {
			console.log(response);
			$('#ShowKafkaStopProducerDetails').append(response);
		},
		error: function(err) {
			console.log(err);		
		}
	 });	
	});
	
       $('#ListKafkaTopics2').click(function(){
	//var user = $('#txtUsername').val();
        //var pass = $('#txtPassword').val();
        //var diskeyText = 'park time?';
	var diskeyText = "";
        $.ajax({
            url: '/_kafkaTopics',
            //data: $('form').serialize(),
            data: {param: diskeyText},
            type: 'POST',
            success: function(response) {
         	console.log(response);
                $('#ShowKafkaTopics').append(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
       }); 

	$('#ListKafkaTopics').click(function(){
	       text = "silly dinghey";
		$.ajax({
			type: "POST",
			url: "/_kafkaTopics",		
			//url: "{{ url_for('templates', filename='watchZookeeper.html') }}",
			//data: {param: text}
			data: {param: text}
			//success: function(response){
			//   output = response;
			//   alert(output);
			//}
			
			}).done(function(text){
			 ;
			//$('p.ShowKafkaTopics').add(text);
			//console.log(text);
			//alert(text);	
			alert(text);
			 
			//alert("who dinghey, ajax?? nice");		
			});
		
	    });
	

	$('#ConsumerLauncher2').click(function(){
	       text = "silly dinghey";
		$.ajax({
			type: "POST",
			url: "/watchZookeeper",		
			//url: "{{ url_for('templates', filename='watchZookeeper.html') }}",
			//data: {param: text}
			data: {param: text}
			
			}).done(function(text){
			//console.log(text);
			//alert(text);	
			alert('done');
			//alert("who dinghey, ajax?? nice");		
			});
		
	    });




/*

	function ConsumerLauncherButton() {
	    alert("Hello Mr bubs!");
	    text = "hi diskey, please sit";
	    alert(text);	
	    $.ajax({
		  type: "POST",
		  url: "/watchzookeeper.html",
		  //text: "os.system('/home/joe/workspace/flasky/kafka-utils/list-topics.sh')",
		  data: {param: text}  
		//		  data: { param: text}
		}).done(function( o ) {
		alert('hello bubbles!');
		   // do something
		console.log(o); 
		});
	}
  */
 
 	

}
);