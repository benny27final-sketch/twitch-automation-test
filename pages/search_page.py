from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.streamer_page import StreamerPage
import time

class SearchPage(BasePage):
    # 行動版搜尋框最常用的定位
    SEARCH_INPUT = (By.XPATH, "//input[@type='search']")

    def search_for(self, term):
        print(f"成功進入搜尋頁面，準備搜尋: {term}")
        time.sleep(3)
        try:
            el = self.find(self.SEARCH_INPUT)
            el.click() # 先點一下確保聚焦
            el.send_keys(term)
            el.send_keys(Keys.ENTER)
            print("已送出搜尋字串")
        except:
            # 如果還是找不到，嘗試用 JS 直接填入值
            print("嘗試用 JS 強制輸入...")
            self.driver.execute_script(f"document.querySelector('input[type=\"search\"]').value='{term}';")
            self.driver.execute_script("document.querySelector('input[type=\"search\"]').dispatchEvent(new KeyboardEvent('keydown', {'key': 'Enter'}));")
        
        return self

    def select_streamer(self):
        time.sleep(5)
        print("搜尋結果加載中，捲動頁面...")
        self.driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)
        # 點擊第一個出現的直播主預覽圖
        first_card = (By.XPATH, "//div[@data-a-target='preview-card-image'] | //a[contains(@href, '/videos/')]")
        self.click(first_card)
        return StreamerPage(self.driver)