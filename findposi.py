import pyautogui

def info():
    data = pyautogui.position()
    print(data)

from time import sleep
sleep(4)
info()