import pyautogui
import time
import webbrowser
import random
import pyperclip
import os
#有时间打开程序
time.sleep(5)
#2双击点赞
# pyautogui.doubleClick(x=1109, y=509, button="left")  # 鼠标在（100，150）位置左击两下
#进入循环
rp=1
# print(pyautogui.size())
# x,y=pyautogui.position()     #返回当前鼠标位置
# print(x,y)
for rp in range(990):
    time.sleep(2)
    pyautogui.press('down') # 按下并松开（轻敲）回车键c
    # pyautogui.press('z') # 按下并松开（轻敲）回车键c
    # pyautogui.typewrite("z")
    time.sleep(random.randint(1, 9)/10)
    pyautogui.click(x=1873, y=570, button="left")  # 鼠标在（100，150）位置左击两下
 
 