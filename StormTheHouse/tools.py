#Library for Getting stuff to work

#Imports
from pynput.mouse import Button #Handling button events
from PIL import ImageGrab as ImageGrab #Library for getting screen images
import numpy as np #Commonly used math library
#Frame of the game
#x=628 y=502
#x2=1164 y2=643


def getImg(): #Function to capture a picture and convert it to a np array
    img = ImageGrab.grab(bbox=(628, 588, 1164, 768)).convert("L") #Get a grayscale image
    img = np.array(img) #Turn the image to a np array
    img.reshape([1164-628,768-588]) #Reshape the picture to a 2D array
    return img #Return the array

def findEnemy(img): #Function to find enemies on screen
    a = img.max() #Local variable for comparison, initialized as the greatest value of the input np array
    if a > 200: #If the highest value is greater 200:
        ind = np.unravel_index(img.argmax(), img.shape) #Find the index of the value
        pos = [627+ind[0]-3,768 +ind[1]-3] #Convert the index to a position on screen and turn values to x,y
        return pos #Return the position on the screen in [x,y]
    else: #If there is no value greater 150 on screen:
        return None #Return None

def on_click(x,y,button,pressed): #If the mouse is pressed while listener is running:
    if button == Button.right: #If the pressed button is equals the right mouse button
        print("Listener stopped") #Print something
        return False #Return False- resulting in collapsing the listener thread

def comparePos(pos,aoe): #Compare 2 arrays- here positions
    q=0 #Local variable
    if pos[0]<aoe[0]+30 and pos[0]>aoe[0]-30: #If the x distance of pos to aoe is between +-30:
        q = q + 1 #Increment q
    if pos[1]<aoe[1]+30 and pos[1]>aoe[1]-30: #If the y distance of pos to aoe is between +-30:
        q = q + 1 #Increment q
    return True if q>1 else False #If q is greater 1 return True otherwise return False
