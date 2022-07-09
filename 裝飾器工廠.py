# 計算1~max的裝飾器工廠
def calculatefactory(max):
    def calculate(callback):
        def run():
            total = 0
            for i in range(max+1):
                total += i
            callback(total)
        return run
    return calculate


@calculatefactory(100)
def show(result):
    print("結果是", result)


@calculatefactory(10)
def showeng(result):
    print("Result is ", result)


show()
showeng()

# def myfactory(base):
#     def mydeco(cb):
#         def run():
#             print("裝飾器程式", base)
#             result = base*2
#             cb(result)
#         return run
#     return mydeco


# @myfactory(3)
# def test(result):
#     print("普通函式程式", result)


# test()
