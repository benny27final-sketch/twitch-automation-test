import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # 建立 Chrome 設定物件
    options = Options()
    
    # 1. 設定 Mobile Emulation (模擬手機裝置)
    # 使用 Pixel 5 可以讓網頁呈現較為現代的行動裝置佈局
    mobile_emulation = {"deviceName": "iPhone X"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    
    # 2. 強制設定視窗大小 (確保按鈕不會因為視窗太小而縮起來)
    options.add_argument("--window-size=400,800")
    
    # 3. 其他優化參數 (避免一些常見的自動化報錯)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # 如果你在執行時不想看到 "Chrome 正受自動測試軟體控制" 的橫幅，可以加這行：
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # 初始化瀏覽器驅動
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # 設定隱含等待 (Implicit Wait) 10 秒，讓 Selenium 找不到元素時會再稍微等一下
    driver.implicitly_wait(10)
    
    yield driver
    
    # 測試結束後關閉瀏覽器
    driver.quit()