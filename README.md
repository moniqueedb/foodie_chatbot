# foodie_chatbot

This repo currently contains the starter files.

1. Clone repo:


$ git clone https://github.com/python-engineer/foodie_chatbot.git


2. Create a virtual environment:

$ python -m venv ./venv/

$ source venv/scripts/activate



3. Install packages

$ pip install flask

$ pip install torch

$ pip install torchvision

$ pip install nltk

$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
Modify intents.json with different intents and responses for your Chatbot


4. Run 
$ (venv) python train.py
This will dump data.pth file. And then run the following command to test it in the console.

$ (venv) python app.py






