from gamegrid import *
from soundsystem import *

# ---------------- classe Animal ----------------
class Animal():

    def __init__(self, imgPath):
        self.imagePath = imgPath


    def showMe(self, x, y):
         bg.drawImage(self.imagePath, x, y)

# ---------------- classe Pet ----------------
class Pet(Animal):

    def __init__(self, imgPath, name):
        Animal.__init__(self, imgPath)
        self.name = name
        self.sound = None

    def tell(self, x, y):
        bg.drawText(self.name, Point(x, y))
        openSoundPlayer(self.sound)
        play()

# ---------------- classe Dog ----------------
class Dog(Pet):

    def __init__(self, imgPath, name):
        Pet.__init__(self, imgPath, name)
        self.name = name
        self.sound = "wav/dog.wav"
        

# ---------------- classe Cat ----------------
class Cat(Pet):

    def __init__(self, imgPath, name):
        Pet.__init__(self, imgPath, name)
        self.name = name
        self.sound = "wav/cat.wav"


makeGameGrid(600, 600, 1, False)
setBgColor(Color.green)
show()
doRun()
bg = getBg()

animals = [Dog("sprites/dog.gif", "Alex"),
           Dog("sprites/dog.gif", "Rex"),
           Cat("sprites/cat.gif", "Xara")]

y = 100
for animal in animals:
    animal.showMe(100, y)
    animal.tell(200, y + 30)    # Which tell()????
    y = y + 200
    delay(1000)