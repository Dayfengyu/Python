#定義類別與屬性
#定義一個類別IO，有supportedSrcs 和 read 兩個屬性
class IO:
    supportedSrcs = ["console","file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not Supported")
        else:
            print("Read from",src)
#使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("Internet")