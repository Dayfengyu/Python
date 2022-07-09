#Series 單維度的資料（試算表中直項的欄位）
#dataframe 雙維度的資料（有欄有列）
#data["欄位名稱"] 取得直向
#data.iloc[列編號] #列編號按順序由0開始累加

import pandas as pd
#建立Series
data = pd.Series([20,10,15])
#基本操作
#print("MAX",data.max())
#print("Median",data.median())
#data = data * 2
#print(data)
#data=data==20 #兩個"="叫比較運算
#print(data)

#建立data frame
data = pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[30000,50000,40000]
})
#基本操作
#print(data["salary"])
#取得特定的列
print(data.iloc[2])