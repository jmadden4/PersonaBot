from . import main
from .forms import SomeForm
import json
import datetime


from flask import jsonify, redirect, render_template, request, url_for, jsonify, make_response, abort

@main.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

question = ""

@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
def index():
	form = SomeForm()	
	#question = form.name.data	
	if request.method == 'POST':
		question = form.name.data		
		from diskeyChatBotResponse import response
		input1=question
		imgPath = url_for('static', filename='sharkDog.jpg')
		resp1 = response(input1)
		imgString = "<img src="+imgPath+" width=120px height=170px></img>" 		
		formResponse =  "<table class=""table"">\
				<thead>\
				 <tr>\
				     <th>Input Value #1</th>\
				     <th>Input Value #2</th>\
				     <th>Diskey Bot Output</th>\
				</thead>\
				</tr>\
				<tbody>\
				<tr>\
				     <td><h4>"+imgString+"</h4></td>\
				     <td><h4>"+question+"</h4></td>\
				     <td><h4>"+resp1+"</h4></td>\
				</tr>\
				</tbody>\
			</table>"
		#resp = "Response from Diskey Bot is: " + "<h3>" + respTemp2 + "</h3><br/>"+ "\n" + "\n" + "Input was: "+respTemp + "\n"
		
		#return redirect(url_for('main.fetchFromChatBot', id=question))
		#return jsonify(data={'question': question})
		#/_fetchFromChatBot/<id>'
		return redirect(url_for('main.index', form=form))
	return render_template('index.html', form=form)

@main.route('/_SubmitForm')
def submitForm():
	return render_template('index.html',form=form)

@main.route('/_askChatBot/<id>', methods=['GET', 'POST'])
def askChatBot(id):
	time_stamp = datetime.datetime.now()
	id = time_stamp	
	id_to_post = id
	#from diskeyChatBotModel import stemmer
	id = -1
	#id = time_stamp
	#id_to_send = 
	question="hello mr bear?"
	print id_to_post
	print id
	#return json.dumps({'status': 'OK','question':question})
	return jsonify(id_to_post)

@main.route('/_askChatBotRandom/<id>', methods=['GET', 'POST'])
def askChatBotRandom(id):
	time_stamp = datetime.datetime.now()
	id = time_stamp	
	id_to_post = id
	#from diskeyChatBotModel import stemmer
	id = -1
	#id = time_stamp
	#id_to_send = 
	question="hello mr bear?"
	print id_to_post
	print id
	#return json.dumps({'status': 'OK','question':question})
	return jsonify(id_to_post)

@main.route('/_fetchFromChatBot/<id>', methods=['GET', 'POST'])
def fetchFromChatBot(id):
	import os, sys, random
	#from diskeyChatBotModel import words	
	#os.system('python /home/joe/workspace/diskey-bot/diskeyChatBotModel.py')
	#resp = words
	#resp = "wowww"
	#os.system('python /home/joe/workspace/diskey-bot/diskeyChatBotResponse.py')
	from diskeyChatBotResponse import response
	input1 = "shark"
	input2 = "pup"
	input3 = "sleepy"
	imgPath1 = url_for('static', filename='sharkDog.jpg')	
	imgPath2 = url_for('static', filename='DiscoDayCare.jpg')
	imgPath3 = url_for('static', filename='tiredTuckedIn.jpg')
	combos = [0, 1, 2]
	comboTemp = random.choice(combos)	
	combo = comboTemp
	imgs = [imgPath1, imgPath2, imgPath3]
	imgTemp = imgs[combo]
	imgPath = imgTemp
	
	imgString = "<img src="+imgPath+" width=120px height=170px></img>" 
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
				     <th>Input Value #1</th>\
				     <th>Input Value #2</th>\
				     <th>Dog Bot Output</th>\
				</thead>\
				</tr>\
				<tbody>\
				<tr>\
				     <td><h4>"+imgString+"</h4></td>\
				     <td><h4>"+respTemp+"</h4></td>\
				     <td><h4>"+respTemp2+"</h4></td>\
				</tr>\
				</tbody>\
			</table>"
	#resp = "Response from Diskey Bot is: " + "<h3>" + respTemp2 + "</h3><br/>"+ "\n" + "\n" + "Input was: "+respTemp + "\n"
	return responseTable


@main.route('/_fetchFromChatBotRandom/<id>', methods=['GET', 'POST'])
def fetchFromChatBotRandom(id):
	import os, sys, random
	#from diskeyChatBotModel import words	
	#os.system('python /home/joe/workspace/diskey-bot/diskeyChatBotModel.py')
	#resp = words
	#resp = "wowww"
	#os.system('python /home/joe/workspace/diskey-bot/diskeyChatBotResponse.py')
	from diskeyChatBotResponse import response
	input1 = "shark"
	input2 = "pup"
	input3 = "sleepy"
	imgPath1 = url_for('static', filename='sharkDog.jpg')	
	imgPath2 = url_for('static', filename='DiscoDayCare.jpg')
	imgPath3 = url_for('static', filename='tiredTuckedIn.jpg')
	combos = [0, 1, 2]
	comboTemp = random.choice(combos)	
	combo = comboTemp
	imgs = [imgPath1, imgPath2, imgPath3]
	imgTemp = imgs[combo]
	imgPath = imgTemp
	
	imgString = "<img src="+imgPath+" width=120px height=170px></img>" 
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
				     <th>Input Value #1</th>\
				     <th>Input Value #2</th>\
				     <th>Dog Bot Output</th>\
				</thead>\
				</tr>\
				<tbody>\
				<tr>\
				     <td><h4>"+imgString+"</h4></td>\
				     <td><h4>"+respTemp+"</h4></td>\
				     <td><h4>"+respTemp2+"</h4></td>\
				</tr>\
				</tbody>\
			</table>"
	#resp = "Response from Diskey Bot is: " + "<h3>" + respTemp2 + "</h3><br/>"+ "\n" + "\n" + "Input was: "+respTemp + "\n"
	return responseTable