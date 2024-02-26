import Constants
import Constants
import globalVariables
from random import randint
from playsound import playsound




def playRandomSound() : 
    
    try : 
        print("Sound is playing...")
        playsound(Constants.LIST_SOUNDS_PATH + globalVariables.listOfSounds[randint(0,len(globalVariables.listOfSounds)-1)])
        print("Sound played!")

    except Exception as e : 
        print(e)