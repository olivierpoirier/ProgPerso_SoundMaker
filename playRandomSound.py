import Constants
import Constants
import globalVariables
from random import randint
from playsound import playsound




def playRandomSound() : 
    
    try : 
        playsound(Constants.LIST_SOUNDS_PATH + globalVariables.listOfSounds[randint(0,len(globalVariables.listOfSounds)-1)])
        
    except Exception as e : 
        print(e)