from datetime import datetime
from random import randint
import globalVariables
from playRandomSound import playRandomSound
import Constants

def soundDirector(mainWindow, labelMinuteToWait, entryChooseMaximumMinute, entryChooseMinimumMinute) :
    try : 
        current_time =datetime.now()

        labelMinuteToWait['text'] = globalVariables.nextTimeSoundWillPlay

        if globalVariables.nextTimeSoundWillPlay >= 60 :
            globalVariables.nextTimeSoundWillPlay = globalVariables.nextTimeSoundWillPlay - 60
            globalVariables.hourHaveChanged = True

        if current_time.minute == 0 :
            globalVariables.hourHaveChanged = False

        if current_time.minute >= globalVariables.nextTimeSoundWillPlay and not globalVariables.hourHaveChanged :
            
            try :
                if int(entryChooseMaximumMinute.get()) >= 0 and int(entryChooseMaximumMinute.get()) <= 60 and int(entryChooseMinimumMinute.get()) >= 0 and int(entryChooseMinimumMinute.get()) < 60 and int(entryChooseMinimumMinute.get()) <= int(entryChooseMaximumMinute.get()) : 
                    globalVariables.nextTimeSoundWillPlay = current_time.minute + randint(int(entryChooseMinimumMinute.get()),int(entryChooseMaximumMinute.get()))
                else :
                    globalVariables.nextTimeSoundWillPlay = current_time.minute + randint(Constants.MIN_MINUTE_TO_WAIT,Constants.MAX_MINUTE_TO_WAIT)
                
            except Exception as e :
                globalVariables.nextTimeSoundWillPlay = current_time.minute + randint(Constants.MIN_MINUTE_TO_WAIT,Constants.MAX_MINUTE_TO_WAIT)
                print(e)
            

            playRandomSound()
        
        print(globalVariables.nextTimeSoundWillPlay)
        mainWindow.after(10000, lambda:soundDirector(mainWindow, labelMinuteToWait, entryChooseMaximumMinute, entryChooseMinimumMinute))
    except Exception as e :
        print(e)
