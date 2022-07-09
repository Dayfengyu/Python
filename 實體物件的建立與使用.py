#透過類別建立：先定義類別，再透過類別建立"實體物件"
#建立>使用：先建立實體物件，才能使用實體屬性
#class 類別名稱:
    #定義初始化函式
    #def __init__(self): 透過操作self來定義實體屬性
#建立實體物件，放入變數obj中
#obj=類別名稱() #呼叫初始化函式

#基本語法：實體物件.實體屬性名稱

# point 實體物件的設計：平面座標上得點
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
#建立第一個實體物件
p1 = point(3,4)
print(p1.x,p1.y)
#建立第二個實體物件
p2 = point(5,6)
print(p2.x , p2.y)

# Fullname 實體物件的設計：分開紀錄姓、名資料的全名
class Fullname:
    def __init__(self,first,last):
        self.first = first
        self.last = last
name1 = Fullname("G.Y.","Lin")
print(name1.first , name1.last)
name2 = Fullname("Y.G.","Lin")
print(name2.first,name2.last)