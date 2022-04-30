import pyautogui
while True:
    a = pyautogui.confirm('ARE YOU DUMB?',buttons=['YES','NO'])
    if a=='YES':
        break   