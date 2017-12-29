# PersonaBot
### Welcome to PersonaBot
*Thank you for visiting!*

A contextual Tensorflow Chatbot wrapped in a Flask application. Thanks to @ugik_ for the tutorial that inspired this project!



### How to run yourself: 

Note - Instructions below are for Ubuntu & python 2.7 w/ pip & virtualenv already installed
 
```bash
virtualenv venv

source venv/bin/activate

pip install -r requirements.txt
```

Run the TensorFlow model (aka train and test model). Note this file is named after Disco, the lab mix. Feel free to call it whatever you'd like
```bash
python diskey-chat-bot-model.py
```
You should see a couple of test cases in the output log. Set the scroll window in your command prompt to 10k+ lines if you want to see the details. 

After the model has completed, check to see if the training_data has been updated (or created). 

Start the Server:
```bash
python app.py runserver
```
Open browser & go to: http://127.0.0.1:5000


