# Point實體物件的設計
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # 定義實體方法
#     def show(self):
#         print(self.x, self.y)

#     def distance(self, tarx, tary):
#         return(((self.x-tarx)**2)+((self.y-tary)**2))**0.5


# p = Point(3, 4)
# p.show()  # 呼叫實體方法/函式
# result = p.distance(0, 0)  # 計算座標3,4到0,0的距離
# print(result)

# file 實體物件的設計
class file:
    def __init__(self, name):
        self.name = name
        self.file = None  # 尚未開啟檔案 初始是None

    def open(self):
        self.file = open(self.name, mode="r", encoding="utf-8")

    def read(self):
        return self.file.read()


# 讀取檔案
f = file("data.txt")
f.open()
print(f.read())
