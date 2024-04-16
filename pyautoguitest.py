#!/usr/bin/env python
'Test page for pyautogui'
'Multiple Monitor fix: https://github.com/asweigart/pyautogui/issues/321'
'My Modified Copy: https://github.com/c0b4a/pyautogui-pyscreenz-fix'

import pyautogui

#used for delaying start from VS scripting
import time
time.sleep(5)

#main screen resolution
print(pyautogui.size())

#move cursor + time taken
pyautogui.moveTo(500, 500, duration = 1)

#move relative to current pos
pyautogui.moveRel(0, 50, duration = 1)

#print position
print(pyautogui.position())

#click(stationary)
pyautogui.click(100, 100)

#drag(relative)
pyautogui.dragRel(0, 100, duration = 1)

#drag(precise)
pyautogui.dragTo(0, 100, duration = 1)

#scroll
pyautogui.scroll(100)

#automate typing(as string)
pyautogui.typewrite('example')

#automate typing(as keyname)(E, left arrow, left cntl)
pyautogui.typewrite(['E', 'left', 'ctrlleft'])

#presses simultaneously
pyautogui.hotkey('ctrlleft', 'a')