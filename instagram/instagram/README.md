# Crawler Instagram

爬取Instagram中搜尋關鍵字後進入頁面的所有貼文與留言，寫入sqlite庫，產出網路圖。

## ．main.py
執行爬蟲。

##### 第一步
  1. 進入Instagram的首頁
  2. 登入
  3. 搜尋關鍵字並進入頁面
  4. 將頁面往下滾動
  5. 取得所有貼文的超連結

##### 第二步，以迴圈逐一對貼文的超連結
  1. 進入貼文的超連結
  2. 點開所有留言與留言的回覆
  3. 取得所有留言的資訊
  4. 取得該篇貼文的資訊
  5. 取得所有圖片的超連結
  6. 紀錄為json格式

##### 第三步
  1. 存為json檔
  2. 下載所有貼文的所有圖片

## ．crawler_helper.py
放置爬蟲的函式。

## ．write_to_db.py
將爬取下來的紀錄轉變為數據框架，並寫入sqlite庫裡。

##### post
|id|url|post_content|post_time|post_like|
|---|---|---|---|---|
|dPCok...|www...|今天....|10000|2023-01-01|

##### comment
|id|comment_username|comment_content|comment_time|comment_like|
|---|---|---|---|---|
|dPCok...|abc...|哇....|50|2023-01-01|


