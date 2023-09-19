from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置浏览器驱动路径
driver_path = "your_driver_path"  # 替换为你的浏览器驱动路径
# 设置要截图的网页地址
url = "https://www.example.com"  # 替换为你要截图的网页地址
# 设置截图保存路径
save_path = "screenshot.png"  # 替换为你要保存的截图路径

# 创建浏览器驱动对象
driver = webdriver.Chrome(driver_path)

# 打开网页
driver.get(url)

# 等待页面加载完成
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# 获取网页内容的高度
scroll_height = driver.execute_script("return document.body.scrollHeight")

# 设置窗口大小为网页内容的高度
driver.set_window_size(driver.get_window_size()["width"], scroll_height)

# 截图保存
driver.save_screenshot(save_path)

# 关闭浏览器
driver.quit()
