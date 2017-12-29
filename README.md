# PersonaBot
### Welcome to PersonaBot

*Visit the [blog post "Personas Meet AI" on Medium](https://medium.com/@jmadden4/persona-development-meets-ai-9bf2603351d8) for more information. 

Thanks to @ugik_ for the tutorial that inspired this project!

A contextual Tensorflow Chatbot wrapped in a Flask application. 

How to Maintain a Persona: [credit usability.gov](https://usability.gov/how-to-and-tools/methods/personas.html)

1) Conduct User Research:
	* Who are your users and why are they using the system? 
	* What behaviors, assumptions, and expectations color their view of the system?
2) Condense the Research: 
	* Look for themes/characteristics that are specific, relevant, and universal to the system and its users.
3) Brainstorm: 
	* Organize elements into persona groups that represent your target users. Name or classify each group.
4) Refine: 
	* Combine and prioritize the rough personas. 
	* Separate them into primary, secondary, and, if necessary, complementary categories. 
	* You should have roughly 3-5 personas and their identified characteristics.
5) Make them realistic: 
	* Develop the appropriate descriptions of each personas background, motivations, and expectations. 
	* Do not include a lot of personal information. Be relevant and serious; humor is not appropriate.



### How to run yourself: 

Note - Instructions below are for Ubuntu & python 2.7 w/ pip & virtualenv already installed
 
```bash
virtualenv venv

source venv/bin/activate

pip install -r requirements.txt
```

Run the TensorFlow model (aka train and test model). 

Note this file creates a 'bag of words' based on 'intents.json'
```bash
python PersonaChatBotModel.py
```
You should see a couple of test cases in the output log. Set the scroll window in your command prompt to 10k+ lines if you want to see the details. 

After the model has completed, check to see if the training_data has been updated (or created). 

Start the Server:
```bash
python app.py runserver
```
Open browser & go to: http://127.0.0.1:5000

Interact with the Persona Bot
* Enter a data point that you'd like to capture OR submit a random data point
* Persona Bot will return a standardized value for your Persona

Current Results (as of 12/29/2017)
![Model Output](https://github.com/jmadden4/PersonaBot/blob/master/app/static/RunModelOutputTerminal.PNG "Model Output")
![Home Page](https://github.com/jmadden4/PersonaBot/blob/master/app/static/PersonaBotMVPHome.PNG "Home Page")
![Server Terminal View](https://github.com/jmadden4/PersonaBot/blob/master/app/static/RunServerTerminalResonse.PNG "A view of your server from the Terminal")
![MVP Success](https://github.com/jmadden4/PersonaBot/blob/master/app/static/PersonaBotMVP.PNG "Home Page now contains a response")



MVP
* update an existing Persona
* render a template that can be shared with project team members

Future State: 
* create a new Persona if as you start to see a new segment
* highlight the personas that you may want to worry less about

In a Galaxy Far, Far Away: 
* Persona Bot Unsupervised Learning with Kafka & Spark Streaming (or another Pipeline) that satisfies the 'holy grail' of persona usage as defined by Usability.Gov 



