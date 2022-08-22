
import random
import json
import torch
import torch.nn as nn
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize



device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as f:
        intents = json.load(f)

FILE ="data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


bot_name = "Foodie Bot"

print("Let's chat! type 'quit' to exit")
while True:
    sentence = input('You: ')
    if sentence == 'quit':
        break


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

    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:

                print(f"{bot_name}: {random.choice(intent['responses'])}")
               
    else:
        print(f"{bot_name}: I do not understand... ")
                

