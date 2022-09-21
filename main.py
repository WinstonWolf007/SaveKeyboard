import os
import time
import pyautogui
import keyboard


btn_start = ""

def started_script():
    global btn_start
    print('press a start button...')
    while True:
        if keyboard.read_key():
            btn_start = keyboard.read_key()
            break
    print("Started when you will have clicked on", btn_start)
    while True:
        if keyboard.read_key() == btn_start:
            break
    time.sleep(2)


allKeyPresed = []


if __name__ == '__main__':
    started_script()

    print('Read started ! (press esc for stop)')

    while True:
        allKeyPresed.append(str(keyboard.read_key()))
        if keyboard.read_key() == btn_start:
            break

    print("Read stop ! (press ctrl for result)")

    while True:
        if keyboard.read_key() == "ctrl":
            break

print(allKeyPresed)
for x in allKeyPresed:
    time.sleep(0.1)
    pyautogui.press(x)
