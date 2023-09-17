import pyautogui
import time

# 设置点击的坐标
x = 500
y = 500

# 设置连点次数
click_count = 10

# 延迟时间（秒）
delay = 1

# 延迟开始点击
time.sleep(5)

# 循环连点
for i in range(click_count):
    pyautogui.click(x, y)
    time.sleep(delay)
