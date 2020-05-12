#@author Maximilian Nasert
import StormTheHouse.tools as tools #Tools
from pynput.mouse import Button, Controller  #Handling the mouse
from pynput.keyboard import Key #Handling key events
from pynput.keyboard import Controller as Con #Handling the keyboard
from pynput.mouse import Listener #Listening to mouse actions
import time #Everything related to time



keyboard = Con() #Keyboard controller
mouse = Controller() #Mouse controller

def agent(): #Game bot
    listener = Listener(on_click=tools.on_click) #Init of listener
    listener.start() #Starting the listener in another thread in a non-blocking fashion
    i=0 #Shoot and wait counter
    aoe=[0,0] #Area of effect memory of last shot to not hit yet falling enemies
    while(listener.running): #As long as the listener is running:
        time.sleep(.03) #Wait 30 ms till next search
        img = tools.getImg() #Get grayscale image to np array
        pos = tools.findEnemy(img) #Search for an enemy and get position: [x,y]
        if pos is not None and not tools.comparePos(pos,aoe): #If the bot didnt shoot at this position lately and there are enemies:
            i = i + 1 #Increment counter
            aoe = pos #Memory is current enemies position
            mouse.position = ((pos[0],pos[1])) #Put the pointer on pos on screen
            mouse.click(Button.left,count=2) #Click the enemy twice
        else: #If the bot did shoot at this position lately or there are no enemies then:
            i = i + 1 #Increment counter
            if i > 50: #If the counter is greater 50
                mouse.position=((973,594)) #Position the mouse around the middle of the game window
                keyboard.press(Key.space) #Press space
                time.sleep(.06) #Wait 60 ms
                keyboard.release(Key.space) #Release space
                i=0 #Reset counter

if __name__ == '__main__':
    #Limits of this program are different units, such as "machine gunners" these seem not to be converted to a scale that surpasses the a > 150(grayscale) clause
    time.sleep(5) #Wait 5000 ms
    agent() #Start the bot