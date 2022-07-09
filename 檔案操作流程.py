#檔案物件=open(檔案路徑,mode=開啟模式)
#讀取模式:r 寫入（儲存）模式:w 讀寫模式:r+
#若中文讀不出來 編碼 encoding="utf-8"
#讀取全部文字 檔案物件.read()
#一次讀取一行 for 變數 in 檔案物件: #從檔案依序讀取
#讀取JSON格式 import json 讀取到的資料=json.load(檔案物件)
#寫入（儲存）文字 檔案物件.write("字串\n")
#寫入json格式 import json json.dump(要寫入的資料,檔案物件)
#關閉檔案 檔案物件.close() 非～常～重～要～
# with open(檔案路徑,mode=開啟模式) as 檔案物件: 讀取或寫入檔案的程式(以上區塊會自動安全的關閉檔案)

#-------------------------------------#

#儲存檔案
#file = open("data.txt",mode="w") #開啟
#file.write("測試中文\n好棒棒") #操作
#file.close() #關閉
#with open("data.txt",mode="w") as file:
 #   file.write("5\n3")
#讀取檔案 把檔案中的數字逐步讀出並計算總和
#sum = 0
#with open("data.txt",mode='r') as file:
 #   for i in file: #行行讀出
  #      sum += int(i)
#print(sum)
#使用json讀取、複寫檔案
import json
#從檔案中讀取json資料 放入變數data裏面
with open("config.json",mode = "r") as file:
    data = json.load(file)
print(data) # data = 字典資料
data["name"] = "New Name" #修改變數中的資料
#把最新資料寫回檔案
with open("config.json",mode = "w") as file:
    json.dump(data,file)
