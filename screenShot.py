import pyautogui
import time
import os
from PIL import Image

# 设置截图保存的文件夹路径
screenshot_folder = "screenshots"
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# 手动打开 Chrome 浏览器并最大化到屏幕可见区域
input("请确保 Chrome 浏览器已打开并最大化在需要截图的页面上，按回车键继续...")
time.sleep(5)

# 记录截图序号
screenshot_count = 1
page_bottom_reached = False

# 开始滚动页面并截图
while not page_bottom_reached:
    # 设置截图保存路径并保存截图
    screenshot_path = os.path.join(screenshot_folder, f"screenshot_{screenshot_count}.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)
    print(f"保存截图：{screenshot_path}")

    # 增加截图计数
    screenshot_count += 1

    # 模拟按下 Page Down 键滚动
    pyautogui.press("pgdn")
    time.sleep(1)  # 等待页面加载完成

    # 检测是否到达页面底部
    if screenshot_count > 2:
        # 比较新截图和前一个截图的像素是否相同
        img1 = Image.open(screenshot_path)
        img2 = Image.open(os.path.join(screenshot_folder, f"screenshot_{screenshot_count - 2}.png"))
        
        if list(img1.getdata()) == list(img2.getdata()):
            page_bottom_reached = True
            print("到达页面底部，结束截图。")
            os.remove(screenshot_path)  # 删除最后一张重复的截图

print("所有截图已保存到文件夹：screenshots")