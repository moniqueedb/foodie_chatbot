from flask import request
from chatbot.nltk_utils import bag_of_words, tokenize, stem
import torch
import json
from chatbot.model import NeuralNet
from neural_net import device, all_words, model, tags, intents, bot_name
import random



def chatbot_msg():
   if request.method == "POST":
            user_data = request.json

            sentence = user_data['msg']


            sentence = tokenize(sentence)

            X = bag_of_words(sentence, all_words)
            X = X.reshape(1, X.shape[0]) # 1 row, 0 columns
            X = torch.from_numpy(X).to(device) # bag of words returns a numpy array


            output = model(X)
            _, predicted = torch.max(output, dim=1)
            tag = tags[predicted.item()]

            # having a look at the probability of softmax in nueralnet

            probs = torch.softmax(output, dim=1)
            prob = probs[0][predicted.item()]

            # now we want to find the corresponding intent if the tag matches one of the tags in our intents.json file then the bot will randomly select a response from choosen tag

            if prob.item() > 0.30:
                for intent in intents["intents"]:
                    if tag == intent["tag"]:

                        print(f"{bot_name}: {random.choice(intent['responses'])}")
                    
            else:
                print(f"{bot_name}: I do not understand... ")
                        