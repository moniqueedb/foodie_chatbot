from flask import Flask, render_template, jsonify, request
import json
import torch
import response_generator
from chatbot.app import NeuralNet


app = Flask(__name__)


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
                response = response_generator.chatbot_msg(message)
                return str(response)

            else:
                return "I do not understand. Please try again."


if __name__=="__main__":
    app.run(debug=True)