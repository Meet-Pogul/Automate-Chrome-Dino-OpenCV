import pyautogui
from PIL import Image, ImageGrab
from time import sleep

black = False
i = 0

def collide(data):
    global i, black
    for i in range(450, 530 + (i//10)):
        for j in range(660, 690):
            # data[i, j] = 0
            if (data[i, j] < 100 and not black) or (data[i, j] > 170 and black):
                pyautogui.press("up")
                i += 1  
                return
    for i in range(500, 550):
        for j in range(570, 630):
            # data[i, j] = 125
            if (data[i, j] < 100 and not black) or (data[i, j] > 170 and black):
                pyautogui.keyDown('down')
                sleep(0.25)
                pyautogui.keyUp("down")
                return
    # return data


if __name__ == "__main__":
    sleep(3)
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        for i in range(300, 370):
            for j in range(200, 250):
                if data[i, j] < 200:
                    black = True
                else:
                    black = False
        collide(data)
        
        # print(black)
        # data = collide(data)
        # image.show()
        # break
