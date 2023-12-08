import win32api, win32con
import keyboard
import time

time.sleep(5)

while not keyboard.is_pressed('k'):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.01)
