# 抓取medium.com的文章資料
import urllib.request as req
import json
# 建立一個request物件，附加request headers的資訊
url = "https://medium.com/_/api/home-feed"
request = req.Request(url, headers={
    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")  # 根據觀察，取得資料是json格式

# 解析json格式的資料，取得每篇文章標題
data = data.replace("])}while(1);</x>", "")
data = json.loads(data)  # 把原始的json資料解析成字典/列表的表示形式
# 取得JSON資料中的文章標題
posts = data["payload"]["references"]["Post"]
for key in posts:
    post = posts[key]
    print(post["title"])
