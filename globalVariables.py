from loadDataFiles import loadDataFileInList
import Constants

global numberBackgroundImage
numberBackgroundImage = 0

global hourHaveChanged
hourHaveChanged = False

global nextTimeSoundWillPlay
nextTimeSoundWillPlay = 69

global listOfImages
listOfImages = loadDataFileInList(Constants.LIST_IMAGES_PATH)

global listOfSounds
listOfSounds = loadDataFileInList(Constants.LIST_SOUNDS_PATH)

global isTimeToPlay1RandomSound
isTimeToPlay1RandomSound = False