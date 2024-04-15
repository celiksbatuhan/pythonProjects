import pyautogui
import time


def message():
    for i in range(5, 0, -1):
        print(f"{i}..")
        time.sleep(1)
        
    for i in range(1, 1001):
        pyautogui.write(f"{i} - I LOVE YOU SO MUCH")
        pyautogui.press("enter")


while True:
    message()
