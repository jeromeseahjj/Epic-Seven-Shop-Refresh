"""
Created on Thu Sep 21 11:07:00 2023

@author: Jerome

Modified off @ema original work on auto shop refresh, to fix edge cases(Included in README). 
"""
from pyautogui import *
import pyautogui
import time
import keyboard

###########
# Global variable
# PAUSE_TIME: Sets the time to wait after each action
# CONFIRM_TIME: Sets the timer to wait for confirm screen to appear
# DRAG_PIXEL: How much to drag/scroll to see the final line in the shop
PAUSE_TIME = 0.3 # Currently is 0.3 seconds. Increase this if your BlueStack is lagging. 
CONFIRM_TIME = 0.5 # Change this if your bluestack is lagging and confirm screen is taking time to appear.
DRAG_PIXEL = 400 # Increase this if you realize you cannot scroll until the last row

coven_counter = 0 # Counts how many convenent summon bought
mystic_counter = 0 # Counts how many mystic summon bought
refresh_counter = 0 # Number of refresh done
###########

###########
# Pyautogui setting
pyautogui.PAUSE = PAUSE_TIME
FAIL_SAFE = True
screen_res = pyautogui.size()

###########

def buy_conven_sum(): 
    Coven_pos = pyautogui.locateOnScreen('new_coven.PNG',confidence=0.98)
    if (Coven_pos) != None:
        print("Buy Covenant Summons.")
        Coven_point=pyautogui.center(Coven_pos)
        pyautogui.click(x=Coven_point[0], y=Coven_point[1], clicks=2, interval=0.05, button='left')
        time.sleep(CONFIRM_TIME)#wait for confirm button
        Buy_button_Covenant_pos=pyautogui.locateOnScreen('Buy_button_Covenant.PNG')
        Buy_button_Covenant_point=pyautogui.center(Buy_button_Covenant_pos)
        pyautogui.click(x=Buy_button_Covenant_point[0], y=Buy_button_Covenant_point[1], clicks=2, interval=0.05, button='left')
        time.sleep(CONFIRM_TIME) # Added to fix edge cases
        return 1
    return 0

def buy_mystic_sum():
    Mystic_pos = pyautogui.locateOnScreen('mystic1.PNG',confidence=0.97)
    if (Mystic_pos) != None:
        print("Buy Mystic Summons.")
        Mystic_point=pyautogui.center(Mystic_pos)
        pyautogui.click(x=Mystic_pos[0]+800, y=Mystic_pos[1]+100, clicks=2, interval=0.05, button='left')
        time.sleep(0.5)#wait for confirm button
        Buy_button_Mystic_pos=pyautogui.locateOnScreen('Buy_button_Mystic.PNG')
        Buy_button_Mystic_point=pyautogui.center(Buy_button_Mystic_pos)
        pyautogui.click(x=Buy_button_Mystic_point[0], y=Buy_button_Mystic_point[1], clicks=2, interval=0.05, button='left')
        time.sleep(CONFIRM_TIME)
        return 1
    return 0

while keyboard.is_pressed('q') == False:
    time.sleep(PAUSE_TIME)
    # Look for conven/mystic
    mystic_counter += buy_mystic_sum()
    coven_counter += buy_conven_sum()

    # Scroll if none is detected
    pyautogui.moveTo(screen_res[0]/2, screen_res[1]/2, duration=0)
    # Drag upwards
    pyautogui.dragTo(screen_res[0]/2, screen_res[1]/2-DRAG_PIXEL, duration=0.3)
    time.sleep(0.1)

    # Check for last line 
    mystic_counter += buy_mystic_sum()
    coven_counter += buy_conven_sum()

    # Refresh
    RB_pos=pyautogui.locateOnScreen('refresh_button.PNG',confidence=0.90)
    time.sleep(PAUSE_TIME)
    RB_point=pyautogui.center(RB_pos)
    pyautogui.click(x=RB_point[0], y=RB_point[1], clicks=2, interval=0.05, button='left')
    time.sleep(PAUSE_TIME)#wait for confirm to appear
    Confirm_pos=pyautogui.locateOnScreen('confirm button.PNG')
    Confirm_point=pyautogui.center(Confirm_pos)
    pyautogui.click(x=Confirm_point[0], y=Confirm_point[1], clicks=2, interval=0.05, button='left')
    time.sleep(PAUSE_TIME)
    refresh_counter+=1
    print("Covenant Summons bought=",coven_counter)
    print("Mystic Summons bought=",mystic_counter)
    print("Refresh Done=",refresh_counter)