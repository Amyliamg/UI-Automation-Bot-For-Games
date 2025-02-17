import cv2
import numpy as np
import pyautogui
import time
from PIL import ImageGrab
import random

pyautogui.FAILSAFE = False

button_template = cv2.imread("button.jpg", 0)
THRESHOLD = 0.8  # 会影响运行速度

def find_and_click():
    
    # 截取屏幕
    screenshot = ImageGrab.grab()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    # 进行模板匹配
    result = cv2.matchTemplate(screenshot, button_template, cv2.TM_CCOEFF_NORMED)
    max_val, max_loc = cv2.minMaxLoc(result) # 只考虑右下角

    # 如果匹配度高于阈值
    if max_val > THRESHOLD:
        x, y = max_loc    
        h, w = button_template.shape   
        center_x, center_y = x + w // 2, y + h // 2  
        print(f"发现按钮，点击位置: ({center_x}, {center_y})")

        # 根据图片位置指定点击位置
        pyautogui.moveTo(center_x+100, center_y+100, duration=0.2)
        pyautogui.click()
        time.sleep(0.5)  # 避免连点过快

if __name__ == "__main__":
    count = 0
    while count < 10: # 跑10次限制
        print("running")
        count += 1
        find_and_click()
        pause_time = random.uniform(0.5, 1.5)  # 随机时间防止被检测
        time.sleep(pause_time)
