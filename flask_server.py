from email import message
from flask import Flask, render_template, request, jsonify
from chatbot.chat import chat_response
import os



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chatbot', methods=["GET","POST"])
def get_bot_response():
    if request.method == "POST":
        #return jsonify(msg="Hello")

        user_data = request.json

        message = user_data['msg']

        response = ""
        if message:
            response = chat_response(message)
            return jsonify(msg=str(response)
)
        else:
            return "Missing data!"


if __name__=="__main__":
    app.run(debug=True)