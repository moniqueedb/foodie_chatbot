from flask import Flask, render_template, jsonify, request
import random
import json
import torch
from chatbot.nltk_utils import bag_of_words, tokenize
from chatbot.model import NeuralNet

app = Flask(__name__)

try:
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

except Exception as e:
	print(e)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chatbot', methods=["GET","POST"])
def get_bot_response():
    if request.method == "POST":
            user_data = request.json

            sentence = user_data['msg']

            message = request.args.get('msg')
            response = ""
            if message:
                response = generate_responses.chatbot_msg(message)
                return str(response)

            else:
                return "I do not understand. Please try again."


if __name__=="__main__":
    app.run(debug=True)