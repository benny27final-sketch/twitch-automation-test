import os
import time
from pages.base_page import BasePage

class StreamerPage(BasePage):
    def take_screenshot(self, name):
        time.sleep(10) # 等待影片加載
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        self.driver.save_screenshot(f"screenshots/{name}")
        print(f"截圖已儲存：screenshots/{name}")