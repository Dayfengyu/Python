def add(n1, n2, cb):
    cb(n1+n2)


def handle1(result):
    print("結果是", result)


def handle2(result):
    print("Result", result)


add(3, 4, handle1)
add(5, 4, handle1)
add(5, 4, handle2)

# def test(arg):
#     arg(1000)  # 呼叫回呼函式，帶入參數

# # 定義一個回呼函式


# def handle(da):
#     print(da)


# test(handle)
