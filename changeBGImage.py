import globalVariables
from PIL import Image
from PIL import ImageTk
import Constants



def changeBackgroundImage(background, frameImage) : 
    
    try : 
        
        globalVariables.numberBackgroundImage += 1

        if globalVariables.numberBackgroundImage >= len(globalVariables.listOfImages) :
            globalVariables.numberBackgroundImage = 0
        
        for i in range(len(globalVariables.listOfImages)) :
            if i == globalVariables.numberBackgroundImage :
                newImage = Image.open(Constants.LIST_IMAGES_PATH + globalVariables.listOfImages[i]).resize((frameImage.winfo_width(),frameImage.winfo_height()))
                newPhotoImage = ImageTk.PhotoImage(newImage)
                break

        background.configure(image=newPhotoImage)
        background.image = newPhotoImage
        
     
    except Exception as e : 
        print(e)