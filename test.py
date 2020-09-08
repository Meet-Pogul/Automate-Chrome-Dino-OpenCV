import pyautogui
from PIL import Image, ImageGrab
from time import sleep
# from numpy import asarray

# def typeMeet():
    # pyautogui.keyDown('m')
    # pyautogui.keyDown('e')
    # pyautogui.keyDown('e')
    # pyautogui.keyDown('t')

# def takeScreenshot():
#     sleep(2)
#     image = ImageGrab.grab()
#     image.show()

def hit(key):
    pyautogui.press(key)
    return

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(300, 415):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(300, 415):
        for j in range(563, 650):
            if data[i, j] < 100:
                hit("up")
                return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    sleep(2)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
            
        # print(asarray(image))
        '''
        # Draw the rectangle for cactus
        for i in range(275, 325):
            for j in range(563, 650):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(250, 300):
            for j in range(410, 563):
                data[i, j] = 171

        image.show()
        break
      '''


# if __name__ == "__main__":
#     # typeMeet()
#     # takeScreenshot()
#     pass