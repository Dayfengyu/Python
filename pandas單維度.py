import pandas as pd

#資料索引
#data = pd.Series([5,4,-2,3,7] ,index=["a","b","c","d","e"]) #index = 索引

#觀察資料
#print("資料型態",data.dtype)
#print("資料數量",data.size)
#print("資料索引",data.index)

#取得資料：根據順序、根據索引
#print(data[2],data[0]) #順序
#print(data["e"],data["b"]) #索引

#數字運算：基本、統計、順序
#print("最大值", data.max())
#print("總和", data.sum())
#print("標準差", data.std())
#print("中位數", data.median())
#print("最大三個數\n", data.nlargest(3))
#print("最小兩個數\n", data.nsmallest(2))

data = pd.Series(["您好","Python","Pandas"])
#字串運算：基本、串接、搜尋、取代
#print(data.str.lower())
#print(data.str.upper())
#print(data.str.len())
#print(data.str.cat(sep=",")) #串接 sep=中間間隔符號
#print(data.str.contains("P")) #搜尋
print(data.str.replace("您好","Hello")) #取代