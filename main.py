from sndhdr import whathdr
import pyautogui as pt 
from time import sleep
import pyperclip
import random

sleep(3)

position1 = pt.locateOnScreen("C:/Users/Ayush Sharma/Dropbox/Whatsapp Chatbot/smile_paperclip.png",confidence=.6)
x = position1[0]
y = position1[1]

#Gets message
def get_message() :
    global x, y 
    position = pt.locateOnScreen("C:/Users/Ayush Sharma/Dropbox/Whatsapp Chatbot/smile_paperclip.png",confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y,duration=.1)
    pt.moveTo(x+40,y-70,duration=.1)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message recieved: "+ whatsapp_message)
    return whatsapp_message

message = get_message()

#Posts    
def post_response(message):
    global x, y 
    position = pt.locateOnScreen("C:/Users/Ayush Sharma/Dropbox/Whatsapp Chatbot/smile_paperclip.png",confidence=.6)
    x = position[0]
    y = position[1]
    
    pt.moveTo(x+200,y+20,duration=.1)
    pt.click()
    pt.typewrite(message, interval=.01)
    pt.typewrite("\n",interval=.01)

#Processes response
def process_response(message):
    hi = ["Hey","Hello!"]
    hey = ["Hi","Hello!"]
    hello = ["Hey","Hi!"]
    if "hey" in message.lower():
        return random.choice(hey)
    elif "hi" in message.lower():
        return random.choice(hi)
    elif "hello" in message.lower():
        return random.choice(hello)
    elif "how are you" in message.lower():
        return "I am good what about you?"
    elif "what you doing" in message.lower():
        return "Nothing much"
    elif "who are you" in message.lower():
        return "I am a Chatbot created by Ayush"
    else:
        return "kuch saukha paa lena si"
    
    
         
processed_message = process_response(message)
post_response(processed_message)

