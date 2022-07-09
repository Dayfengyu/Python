# 建立生成器函式
# def test():
#     yield 5


# # 呼叫回傳生成器
# gen = test()

# # 搭配for迴圈
# for d in gen:
#     print(d)

def generateEven(maxnum):
    num = 0
    while num <= maxnum:
        yield num
        num += 2


evengenerator = generateEven(10)
for data in evengenerator:
    print(data)
