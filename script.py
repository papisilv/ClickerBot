from pynput.mouse import  Button, Controller
from pyautogui import press, typewrite, hotkey
import time

mouse = Controller();

locationMouse = (145,289)
print('The current pointer position is {0}'.format(
    mouse.position))
mouse.position = locationMouse
mouse.click(Button.left, 1)
time.sleep(1)

locationMouse = (285,519)
print('The current pointer position is {0}'.format(
    mouse.position))
mouse.position = locationMouse
mouse.click(Button.left, 1)
time.sleep(1)

locationMouse = (583,456)
print('The current pointer position is {0}'.format(
    mouse.position))
mouse.position = locationMouse
mouse.click(Button.left, 1)
time.sleep(1)



locationMouse = (168,574)
print('The current pointer position is {0}'.format(
    mouse.position))
mouse.position = locationMouse
mouse.click(Button.left, 1)
typewrite('Facebook Bot', interval=0.25)
time.sleep(1)

hotkey('tab')
typewrite('10000', interval=0.25)

hotkey('tab')
press("down")
press(["tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab","tab"])
press("enter")
time.sleep(1)
press("tab")
time.sleep(1)
press("down")
time.sleep(1)
press("enter")
time.sleep(1)
press("tab")
time.sleep(1)
typewrite('PCBOT', interval=0.25)
press(["tab","tab"])
time.sleep(1)
typewrite('Facebook bot', interval=0.25)
time.sleep(1)
press(["tab","tab","tab","tab","tab"])
