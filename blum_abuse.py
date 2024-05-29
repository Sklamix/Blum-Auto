# Script By Sklam1x
from pyautogui import *
import pygetwindow as gw
import colorama
from colorama import Fore, Back, Style
import pyautogui
import time
import keyboard
import random
import sys
from pynput.mouse import Button, Controller

mouse = Controller()
time.sleep(0.5)


def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)


window_name = input(Back.YELLOW + '| Script By Sklam1x' + Style.RESET_ALL)
window_name = input(Fore.BLUE + '| Window Name (1 - TelegramDesktop): ' + Style.RESET_ALL)

if window_name == '1':
    window_name = "TelegramDesktop"

check = gw.getWindowsWithTitle(window_name)
if not check:
    print(Back.RED + "| Window - Don't find!" + Style.RESET_ALL)
else:
    print(Back.GREEN + "| Window Find - | Press 'q' to pause" + Style.RESET_ALL)

telegram_window = check[0]
paused = False

while True:
    if keyboard.is_pressed('esc'):
        print(Fore.RED + '| Program Stopped' + Style.RESET_ALL)
        break

    if keyboard.is_pressed('q'):
        paused = not paused
        if paused:
            print(Fore.CYAN + '| Pause' + Style.RESET_ALL)
        else:
            print(Fore.GREEN + '| Start')
        time.sleep(0.2)

    if paused:
        continue

    window_rect = (
        telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height
    )

    if telegram_window != []:
        try:
            telegram_window.activate()
        except:
            telegram_window.minimize()
            telegram_window.restore()

    scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))

    width, height = scrn.size
    pixel_found = False
    if pixel_found == True:
        break

    for x in range(0, width, 20):
        for y in range(0, height, 20):
            r, g, b = scrn.getpixel((x, y))
            if (b in range(0, 125)) and (r in range(102, 220)) and (g in range(200, 255)):
                screen_x = window_rect[0] + x
                screen_y = window_rect[1] + y
                click(screen_x + 4, screen_y)
                time.sleep(0.001)
                pixel_found = True
                break
# Script By Sklam1x
