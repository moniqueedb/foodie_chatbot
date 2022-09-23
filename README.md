# Foodie Chatbot

![image](https://user-images.githubusercontent.com/104881370/191832408-c31d16f4-07a1-4b70-a23f-923476800442.png)

Foodie Chatbot is a deep-learning chatbot designed to help restaurants attract and engage with their patrons. Customers can ask questions about the restaurant's hours, menu, special offerings (e.g. vegetarian and vegan options), payment methods, and more. The chatbot was created using a PyTorch model and Flask-based UI.

### Installation and Set-up

1. Install python (version 3.6.13 is compatible; other versions may also be used)
2. Clone the github repository using GitBash ```git clone https://github.com/moniqueedb/foodie_chatbot.git``` or using any other method.
3. Create a virtual environment. ``` python -m venv myvenv ```
4. Activate your virtual environment. ```source myvenv/Scripts/activate```
5. Set up virtual environment with the packages included in the 'requirements.txt' file. We recommend running: ```pip install -r requirements.txt```
6. Install the nltk punkt package: ```python update_punkt_train.py punkt```

### Train the Model
The chatbot is trained based on the 'intents.json' file. Training the model produces a 'data.pth' file, which is needed for the chatbot to generate responses.

1. To train the model, run: ```python update_punkt_train.py train```
2. Simply running ```python update_punkt_train.py``` will return the response, "Re-training is not required."

OPTIONAL: Modify intents.json with customized intents and responses for your restaurant chatbot. The chatbot must be retrained each time changes are made to the 'intents.json' file.

### Run the Flask App

1. To run the flask app, run: ```python flask_server.py```
2. Open the flask app in your local server.
3. Click on the chatbot icon in the bottom right corner.
4. Start chatting. Try typing into the textbox: "Hello," "What's on your menu?," "I'm vegetarian," or "How do I pay?"). Text entries can be submitted either by clicking on the "Send" button on the UI or pressing the enter key on your keyboard.
5. For payments, the chatbot presents a hyperlink which redirects the customer to a payment page. The user can select the quantity of each food item to make a payment for their purchase. (To simulate a payment, use any of the card numbers listed on Stripe's documentation: https://stripe.com/docs/testing)
