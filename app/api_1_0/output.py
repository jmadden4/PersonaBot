from flask import jsonify, request, g, url_for, current_app
from . import api

@api.route('/_askChatBot/<id>', methods=['GET', 'POST'])
def askChatBot(id):
	time_stamp = datetime.datetime.now()
	id = time_stamp	
	id_to_post = id
	id = -1
	question="hello mr bear?"
	print id_to_post
	print id
	return jsonify(id_to_post)



@api.route('/_fetchFromChatBot/<id>', methods=['GET', 'POST'])
def fetchFromChatBot(id):
	import os, sys, random
	from PersonaChatBotResponse import response
	input1 = "Tablet"
	input2 = "PC"
	input3 = "Mobile"
	imgPath1 = url_for('static', filename='sharkDog.jpg')	
	imgPath2 = url_for('static', filename='DiscoDayCare.jpg')
	imgPath3 = url_for('static', filename='tiredTuckedIn.jpg')
	combos = [0, 1, 2]
	comboTemp = random.choice(combos)	
	combo = comboTemp
	imgs = [imgPath1, imgPath2, imgPath3]
	imgTemp = imgs[combo]
	imgPath = imgTemp
	imgString = "<img src="+imgPath+" width=140px height=170px></img>" 
	inputOptions = [input1, input2, input3]	
	resp1 = response(input1)
	resp2 = response(input2)
	resp3 = response(input3)
	respInput = [input1, input2, input3]
	#respTemp = random.choice(respInput)
	respTemp = respInput[combo]
	respTemp2 = response(respTemp)
	responseTable =  "<table class=""table"">\
				<thead>\
				 <tr>\
				     <th>User Photo</th>\
				     <th>Variable Type</th>\
				     <th>Input Variable</th>\
				     <th>Persona Bot Output</th>\
				</thead>\
				</tr>\
				<tbody>\
				<tr>\
				     <td><h4>"+imgString+"</h4></td>\
				     <td><h4>Technology</h4></td>\
				     <td><h4>"+respTemp+"</h4></td>\
				     <td><h4>"+respTemp2+"</h4></td>\
				</tr>\
				</tbody>\
			</table>"
	#resp = "Response from Diskey Bot is: " + "<h3>" + respTemp2 + "</h3><br/>"+ "\n" + "\n" + "Input was: "+respTemp + "\n"
	return responseTable