
# coding: utf-8

# In[1]:


# things we need for NLP
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

# things we need for Tensorflow
import numpy as np
import tflearn
import tensorflow as tf
import random


# In[2]:


# restore all of our data structures
import pickle
data = pickle.load( open( "training_data", "rb" ) )
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']

# import our chat-bot intents file
import json
with open('intents.json') as json_data:
    intents = json.load(json_data)


# In[3]:


# Build neural network
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# Define model and setup tensorboard
model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')


# In[4]:


def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))


# In[5]:


p = bow("is your shop open today?", words)
print (p)
print (classes)


# In[6]:


# load our saved model
model.load('./model.tflearn')


# In[7]:


# create a data structure to hold user context
context = {}

ERROR_THRESHOLD = 0.25
def classify(sentence):
    # generate probabilities from the model
    results = model.predict([bow(sentence, words)])[0]
    # filter out predictions below a threshold
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], r[1]))
    # return tuple of intent and probability
    return return_list

def response(sentence, userID='123', show_details=False):
    results = classify(sentence)
    # if we have a classification then find the matching intent tag
    if results:
        # loop as long as there are matches to process
        while results:
            for i in intents['intents']:
                # find a tag matching the first result
                if i['tag'] == results[0][0]:
                    # set context for this intent if necessary
                    if 'context_set' in i:
                        if show_details: print ('context:', i['context_set'])
                        context[userID] = i['context_set']

                    # check if this intent is contextual and applies to this user's conversation
                    if not 'context_filter' in i or                         (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                        if show_details: print ('tag:', i['tag'])
                        # a random response from the intent
                        some_random_response = random.choice(i['responses'])
                        print some_random_response
			return random.choice(i['responses'])
            results.pop(0)


# In[8]:


classify('is your shop open today?')


# In[9]:


response('is your shop open today?')


# In[10]:


response('do you take cash?')


# In[11]:


response('what kind of mopeds do you rent?')


# In[12]:


response('Goodbye, see you later')


# In[13]:


context


# In[14]:


response('we want to rent a moped')


# In[15]:


# show context
context


# In[16]:


response('today')


# In[17]:


classify('today')


# In[18]:


# clear context
response("Hi there!", show_details=True)


# In[19]:


response('today')
classify('today')


# In[20]:


response("thanks, your great")

# clear context
response("Hi there!", show_details=True)

classify('Shark i presume?')
response('Shark i presume?', show_details=True)
classify('Dog i presume?')
response('Dog i presume?', show_details=True)
#response('Shark i presume?', show_details=True)

