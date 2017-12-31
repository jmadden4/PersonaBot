from . import main
from .forms import SomeForm
import json
import datetime


from flask import jsonify, redirect, render_template, request, url_for, jsonify, make_response, abort, flash
from flask_restful import Resource, Api

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.before_request
def csrf_protect():
    if request.method == "POST":
	token = session.pop('_csrf_token', None)
	if not token or token != request.form.get('_csrf_token'):
	    abort(403)
def generate_csrf_token():
	    if '_csrf_token' not in session:
		session['_csrf_token'] = some_random_string()
	    return session['_csrf_token']






@main.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

question = ""

@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
#@main.route('/output', methods=['GET', 'POST'])
def index():
	form = SomeForm()
	if form.validate_on_submit():
		#do nothing
		app.jinja_env.globals['csrf_token'] = generate_csrf_token
		form.reset()
		# seriously do nothing	
	return render_template('index.html',form=form)

@main.route('/2', methods=['GET', 'POST'])
@main.route('/index2', methods=['GET', 'POST'])
def index2():
	form = SomeForm()	
	#question = form.name.data	
	if request.method == 'POST':
		question = form.name.data
		print question		
		from PersonaChatBotResponse import response
		input1=question
		imgPath = url_for('static', filename='sharkDog.jpg')
		resp1 = response(input1)
		imgString = "<img src="+imgPath+" width=120px height=170px></img>" 		
		formResponse =  "<table class=""table"">\
				<thead>\
				 <tr>\
				     <th>Input Value #1</th>\
				     <th>Input Value #2</th>\
				     <th>Persona Bot Output</th>\
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
		#return redirect(url_for('main.index', form=form))
		#return render_template('index.html', form=form, question=question)
		abort
	return render_template('index.html', form=form)

#@main.route('/_SubmitForm')
#def submitForm():
#	return render_template('index.html',form=form)

@main.route('/_askChatBot/<id>', methods=['GET', 'POST'])
def askChatBot(id):
	time_stamp = datetime.datetime.now()
	id = time_stamp	
	id_to_post = id
	id = -1
	question="hello mr bear?"
	print id_to_post
	print id
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
	question="no tech?"
	print id_to_post
	print id
	return jsonify(id_to_post)

@main.route('/_fetchFromChatBot/<id>', methods=['GET', 'POST'])
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


@main.route('/_fetchFromChatBotRandom/<id>', methods=['GET', 'POST'])
def fetchFromChatBotRandom(id):
	import os, sys, random
	#from diskeyChatBotModel import words	
	#os.system('python /home/joe/workspace/diskey-bot/diskeyChatBotModel.py')
	#resp = words
	#resp = "wowww"
	#os.system('python /home/joe/workspace/diskey-bot/diskeyChatBotResponse.py')
	from PersonaChatBotResponse import response
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