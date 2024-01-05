
'''
import
'''
import sys
import json
import crawler_helper as ch
from selenium import webdriver
import json
from pathlib import Path
base_path = Path(r'%notebook').absolute().parent.parent.parent.parent
with open(fr"{base_path}\config.json", "r") as f:
    config = json.load(f)

'''
參數
'''
# 要搜尋的關鍵字
keyword = 'senyeyezi'


'''
config
'''

# chromedriver 的路徑, 不是瀏覽器
PATH_CHROMEDRIVER = config['path']['chromedriver']
# instagram 的首頁
URL_INSTAGRAM = config['url']['instagram']
# 登入帳號
ACCOUNT_USERNAME = config['account']['instagram_username']
# 登入密碼
ACCOUNT_PASSWORD = config['account']['instagram_password']





if __name__ == '__main__':
    
    '''
    瀏覽器工具的設置
    '''
    # 啟動瀏覽器工具的選項
    options = webdriver.ChromeOptions()
    # # 不開啟實體瀏覽器背景執行
    # options.add_argument('--headless')
    # 最大化視窗
    options.add_argument('--start-maximized')
    # 開啟無痕模式
    options.add_argument('--incognito')
    # 禁用彈出攔截
    options.add_argument('--disable-popup-blocking')
    options.chrome_executable_path = config['path']['chromedriver']
    
    
    
    '''
    數據放置
    '''
    # 放置爬取的資料
    list_data = []
    
    # 放置圖片的超連結 
    set_link = set()
    
    # 設定 set 物件, 放置圖片連結, 協助過濾重複的元素
    # - 因為 IG 會把只留當前圖片與前一張與後一張, 總共3張, 其他不會留
    set_temp = set()
    
    
    
    '''
    selenium
    '''
    # 啟用
    driver = webdriver.Chrome(options=options)
    # 前往首頁
    driver.get(URL_INSTAGRAM)
    
    ch.login(driver, account_username=ACCOUNT_USERNAME, account_password=ACCOUNT_PASSWORD)
    # 再次前往首頁
    driver.get(URL_INSTAGRAM)
    ch.notice(driver)
    ch.search(driver, keyword)
    list_link = ch.scroll_link(driver, set_link, limit=3)
    
    # for link in list_link[0:5]:
    for link in list_link:
    # for link in list_link_continue_1:
        ch.parse(driver, set_temp, link, list_data)
    
    ch.path_folder_make(keyword)
    ch.save_json(keyword, list_data)
    str_json = ch.open_json(keyword)
    ch.download_img(keyword, str_json)

    # 關閉頁面
    driver.close()

