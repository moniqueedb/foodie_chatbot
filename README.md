# foodie_chatbot

This repo currently contains the starter files.

1. Clone repo:


$ git clone https://github.com/python-engineer/foodie_chatbot.git


2. Create a virtual environment:


$ python -m venv ./venv/

$ source venv/scripts/activate



3. Install packages:


$ pip install flask

$ pip install torch

$ pip install torchvision

$ pip install nltk

$ (venv) python

>>> import nltk

>>> nltk.download('punkt')

Modify intents.json with different intents and responses for your Chatbot


4. Run:

$ (venv) python update_punkt_train.py

* This file allows the user to input command line arguments. Arguments can be written in any order after the file name.
* For first-time users, please download the nltk punkt package by running the following ```python update_punkt_train.py punkt```
* To train the model, run: ```python update_punkt_train.py train```
* To download punkt AND train, run: ```python update_punkt_train.py punkt train```


$ (venv) python app.py






