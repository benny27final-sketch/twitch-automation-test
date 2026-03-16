from pages.home_page import HomePage

def test_twitch_sc2_flow(driver):
    # 1. 前往 Twitch
    driver.get("https://m.twitch.tv")
    
    home = HomePage(driver)
    
    # 2 & 3. 點擊搜尋並輸入 StarCraft II
    search_page = home.go_to_search().search_for("StarCraft II")
    
    # 4. 捲動頁面 (這裡執行 2 次)
    search_page.scroll_down(2)
    
    # 5. 選擇一個直播主
    streamer_page = search_page.select_streamer()
    
    # 6. 等待加載並截圖
    streamer_page.take_screenshot("starcraft2_streamer.png")