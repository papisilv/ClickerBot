from pynput.mouse import  Button, Controller
from pyautogui import press, typewrite, hotkey
import time

mouse = Controller();

locationMouse = (1109,742)
print('The current pointer position is {0}'.format(
    mouse.position))
mouse.position = locationMouse
mouse.click(Button.left, 1)



for x in range(40):
  print(typewrite('Spaming..', interval=0.02))
  press("enter")
