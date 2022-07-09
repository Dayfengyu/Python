# 定義一個裝飾器算1~50總和
def calculate(callback):
    def run():
     # 裝飾器想要執行的程式碼
        result = 0
        for n in range(51):
            result += n
            # 把計算結果透過參數傳到被裝飾的普通函式中
        callback(result)
    return run

# 使用裝飾器


@calculate
def show(n):
    print("結果是", n)


@calculate
def showEng(n):
    print("Result is", n)


show()
showEng()

# 定義裝飾器
# def mydeco(cb):
#     def run():
#         print("裝飾器中的程式碼")
#         cb(3) #被裝飾的函式
#     return run
# # 使用裝飾器
# @mydeco
# def test(n):
#     print("普通函式的程式碼", n)
# test()
