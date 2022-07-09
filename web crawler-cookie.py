# 抓取PTT網頁原始碼
import bs4
import urllib.request as req


def getdata(url):
    # 建立一個request物件，附加Request Header的資訊
    ###超級重要###
    request = req.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # 解析原始碼，取得每篇文章的標題
    root = bs4.BeautifulSoup(data, "html.parser")  # 讓套件協助解析html文件
    title = root.find_all("div", class_="title")  # 尋找所有 class=title的div標籤
    for titles in title:
        if titles.a != None:  # 如果標題包含a標籤(沒被刪除)，印出來
            print(titles.a.string)
    # 抓去上一頁的連結
    nextLink = root.find("a", string="‹ 上頁")  # 找到內文是 < 上頁的a標籤
    return(nextLink["href"])


# 主程序:抓取多個頁面的標題
pageurl = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count < 3:
    pageurl = "https://www.ptt.cc" + getdata(pageurl)
    count += 1
