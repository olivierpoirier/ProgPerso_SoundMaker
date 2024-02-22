import os

def loadDataFileInList(path) : 
    try : 
        listData = []
        for nameFile in os.listdir(path):
            if os.path.isfile(os.path.join(path, nameFile)):
                listData.append(nameFile)
    
    except Exception as e:
        print(e)

    finally :
        return listData

