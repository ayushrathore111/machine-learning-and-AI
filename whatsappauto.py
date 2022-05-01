import pyautogui
import os 
import time
import keyboard

who = input("enter the name jisko ghumana h message...: ")
mess = input("kya mess bheju sir .....: ")
os.startfile('C:\\Users\\Neelesh\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
time.sleep(9)
pyautogui.click(x=305, y=135)
keyboard.write(who)
time.sleep(2)
pyautogui.click(x=250, y=285)
time.sleep(2)
pyautogui.click(x=783, y=964)
time.sleep(2)
keyboard.write(mess)
keyboard.press('enter')



