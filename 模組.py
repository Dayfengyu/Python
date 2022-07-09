#隨機模組
import random
#data = random.sample([1,5,6,10,20],3) #隨機選取
#print(data)
#隨機調換順序
#data = [1,5,8,20]
#random.shuffle(data)
#print(data)
#隨機取得亂數
#data = random.uniform(60,100) #60~100之間亂數
#print(data)
#取得常態分配亂數
#data = random.normalvariate(100,10) #(平均數,標準差) 多數在90-110
#print(data)

#統計模組
import statistics as s
data  = s.mean([1,2,3,4,5,8,10]) #平均數
data  = s.median([1,2,3,4,5,8,10]) #中位數
data  = s.stdev([1,2,3,4,5,8,10]) #標準差
print(data)
