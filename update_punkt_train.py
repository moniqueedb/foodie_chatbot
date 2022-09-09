import sys
from chatbot.train import train_chatbot
from required_modules.download_punkt import install_library

#Trains chatbot using command line argument 'train'
def updatemodel():
    train_chatbot()

# Installs punkt using command line argument 'punkt'
def download_punkt():
    install_library()

def main():
    args = sys.argv[1:]

    if 'punkt' in args:
        download_punkt()
        
    if 'train' in args:
        updatemodel()
    else:
        print('Re-training is not required.')
 
if __name__=="__main__":
    main()
