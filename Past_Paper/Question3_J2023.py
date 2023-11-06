Animal = []
Colour = []
global AnimalTopPointer
global ColourTopPointer
AnimalTopPointer = 0
ColourTopPointer = 0


def PushAnimal(DataToPush):
    global AnimalTopPointer
    global ColourTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal.append(DataToPush)
        AnimalTopPointer += 1
        return True
    
def PopAnimal():
    global AnimalTopPointer
    global ColourTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData
    
def ReadData():
    try:
        global AnimalTopPointer
        global ColourTopPointer

        AnimalFile = open("AnimalData.txt", 'r')
        for thisLine in AnimalFile:
            PushAnimal(thisLine)
        AnimalFile.close()

        ColourFile = open('ColourData.txt', 'r')
        for thisLine in ColourFile:
            PushColour(thisLine)
        ColourFile.close()
    except IOError:
        print("file not found")

def PushColour(DataToPush):
    global AnimalTopPointer
    global ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour.append(DataToPush)
        ColourTopPointer += 1
        return True
    
def PopColour():
    global AnimalTopPointer
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData
    
def OutputItem():
    global AnimalTopPointer
    global ColourTopPointer
    AnimalPoped = PopAnimal()
    ColourPoped = PopColour()
    if ColourPoped == "":
        print("No colour")
        PushAnimal(AnimalPoped)
    else:
        if AnimalPoped == "":
            print("No Animal")
            PushColour(ColourPoped)
        else:
            ColourPoped = ColourPoped.strip("\n")
            AnimalPoped = AnimalPoped.strip("\n")
            print(f"{ColourPoped} {AnimalPoped}")

def main():
    ReadData()
    for _ in range(4):
        OutputItem()

main()
