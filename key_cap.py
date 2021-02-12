# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 21:05:11 2021

@author: kristofer
"""
import datetime
from pynput.keyboard import Key, Listener


currently_pressed_key = None

keys_press = list()

def on_press(key):
    global currently_pressed_key
    if key == currently_pressed_key:
        print('{0} repeated'.format(key))
    else:
        print('{0} pressed'.format(key))
        currently_pressed_key = key
        d = datetime.datetime.now()
        keys_press.append(('{0}'.format(key), d.time().strftime('%H:%M:%S')))

def on_release(key):
    global currently_pressed_key
    print('{0} release'.format(key))
    currently_pressed_key = None
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()