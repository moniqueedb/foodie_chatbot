import random
import json
import torch
from chatbot.nltk_utils import bag_of_words, tokenize
from chatbot.model import NeuralNet

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('chatbot/intents.json', 'r') as f:
    intents = json.load(f)

FILE = "data.pth"
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


# chat
bot_name = "Foodie Bot"
#print("Let's chat! type 'quit' to exit")
#while True:
def chat_response(sentence):
    #sentence = input('You: ')
    if sentence == 'quit':
        return('quit') #TODO: quit must be handled by response_generator

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        return(f"{bot_name}: I do not understand...")
