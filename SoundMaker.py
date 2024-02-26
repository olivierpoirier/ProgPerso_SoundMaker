from tkinter import Tk
from tkinter import Frame
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from PIL import Image
from PIL import ImageTk
from changeBGImage import changeBackgroundImage
from soundDirector import soundDirectorForTimedSound
from soundDirector import soundDirectorForButtonSoundClicked
from datetime import datetime
from random import randint
import globalVariables
import Constants
from playRandomSound import playRandomSound
import threading



def make1SoundPlay() :
    globalVariables.isTimeToPlay1RandomSound = True

try : 
    mainWindow = Tk()
    mainWindow.maxsize(Constants.WIDTH_OF_WIN,Constants.HEIGHT_OF_WIN)
    mainWindow.minsize(Constants.WIDTH_OF_WIN,Constants.HEIGHT_OF_WIN)
    mainWindow.title('SoundMaker')
    mainWindow.resizable(False,False)

    mainWindow.iconphoto(True, ImageTk.PhotoImage(Image.open(Constants.LIST_IMAGES_PATH + globalVariables.listOfImages[0])))

    mainFrameLeft = Frame(mainWindow, width=Constants.WIDTH_OF_SECOND_MAIN_FRAME, height=Constants.HEIGHT_OF_WIN, bg='red')
    mainFrameRight = Frame(mainWindow, width=Constants.WIDTH_OF_SECOND_MAIN_FRAME, height=Constants.HEIGHT_OF_WIN, bg='blue')
    
    frameDisplayText = Frame(mainFrameLeft, width=Constants.WIDTH_OF_IMAGE_FRAME, height=Constants.HEIGHT_OF_TEXT_FRAME, bg=Constants.BACKGROUND_COLOR,highlightbackground=Constants.BORDER_COLOR, highlightthickness=Constants.BORDER_TICKNESS)
    labelMinuteToWait = Label(frameDisplayText, text=globalVariables.nextTimeSoundWillPlay, bg = Constants.BACKGROUND_COLOR, font=Constants.FONT,fg=Constants.COLOR_TEXT)
    

    frameImage = Frame(mainFrameLeft, width=Constants.WIDTH_OF_IMAGE_FRAME, height=Constants.WIDTH_OF_WIN, bg=Constants.BACKGROUND_COLOR, highlightbackground=Constants.BORDER_COLOR, highlightthickness=Constants.BORDER_TICKNESS)
    image = Image.open(Constants.LIST_IMAGES_PATH + globalVariables.listOfImages[0]).resize((Constants.WIDTH_OF_WIN, Constants.WIDTH_OF_WIN))
    bgimg = ImageTk.PhotoImage(image)
    background = Button(frameImage,image=bgimg, width=Constants.WIDTH_OF_WIN, height=Constants.WIDTH_OF_WIN, command=lambda : changeBackgroundImage(background, frameImage))


    frameOptions = Frame(mainFrameRight, width=Constants.WIDTH_OF_OPTION_FRAME, height=Constants.HEIGHT_OF_WIN, bg=Constants.BACKGROUND_COLOR_OPTIONS, highlightbackground=Constants.BORDER_COLOR, highlightthickness=Constants.BORDER_TICKNESS)
    labelExplainOption1 = Label(frameOptions, text='This is to set the maximum', bg=Constants.BACKGROUND_COLOR_OPTIONS)
    labelExplainOption2 = Label(frameOptions, text='and minimum time to wait', bg=Constants.BACKGROUND_COLOR_OPTIONS)
    labelExplainOption3 = Label(frameOptions, text='before a sound will play.', bg=Constants.BACKGROUND_COLOR_OPTIONS)
    labelExplainOption4 = Label(frameOptions, text='Only enter positive', bg=Constants.BACKGROUND_COLOR_OPTIONS)
    labelExplainOption5 = Label(frameOptions, text='numbers or nothing will', bg=Constants.BACKGROUND_COLOR_OPTIONS)
    labelExplainOption6 = Label(frameOptions, text='happend. Min : 0 min, ', bg=Constants.BACKGROUND_COLOR_OPTIONS)
    labelExplainOption8 = Label(frameOptions, text='Max : 60 min. ', bg=Constants.BACKGROUND_COLOR_OPTIONS)
    labelChooseMinimumMinute = Label(frameOptions, text='Minimum time (in min) : ', bg=Constants.BACKGROUND_COLOR_OPTIONS)
    entryChooseMinimumMinute = Entry(frameOptions)
    entryChooseMinimumMinute.insert(1, Constants.MIN_MINUTE_TO_WAIT)
    labelChooseMaximumMinute = Label(frameOptions, text='Maximum time (in min) : ', bg=Constants.BACKGROUND_COLOR_OPTIONS)
    entryChooseMaximumMinute = Entry(frameOptions)
    entryChooseMaximumMinute.insert(1, Constants.MAX_MINUTE_TO_WAIT)
    labelExplainOption7 = Label(frameOptions, text='Play random sound : ', bg=Constants.BACKGROUND_COLOR_OPTIONS)


    buttonPlayRandomSound = Button(frameOptions, text='Play!', command=make1SoundPlay)


    labelMinuteToWait.pack(side='top')
    background.pack(side='top')
    frameDisplayText.pack(side='top')
    frameImage.pack(side='bottom')
    frameOptions.pack(side='right')

    mainFrameLeft.pack(side='left')
    mainFrameRight.pack(side='right')

    labelExplainOption1.pack(side='top')
    labelExplainOption2.pack(side='top')
    labelExplainOption3.pack(side='top')
    labelExplainOption4.pack(side='top')
    labelExplainOption5.pack(side='top')
    labelExplainOption6.pack(side='top')
    labelExplainOption8.pack(side='top')
    labelChooseMinimumMinute.pack(side='top')
    entryChooseMinimumMinute.pack(side='top')
    labelChooseMaximumMinute.pack(side='top')
    entryChooseMaximumMinute.pack(side='top')
    labelExplainOption7.pack(side='top')
    buttonPlayRandomSound.pack(side='top')

    frameDisplayText.pack_propagate(False)
    frameImage.pack_propagate(False)
    frameOptions.pack_propagate(False)



    threading.Thread(target=soundDirectorForTimedSound(mainWindow, labelMinuteToWait, entryChooseMaximumMinute, entryChooseMinimumMinute), daemon=True).start()
    threading.Thread(target=soundDirectorForButtonSoundClicked(mainWindow), daemon=True).start()

    mainWindow.mainloop()
except Exception as e :
    print(e)
