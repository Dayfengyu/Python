# 例外處理情節:轉換資料型態失敗
# 使用者如果輸入不是數字，請他重新輸入到是數字
while True:
    data = input("請輸入一個數字：")
    try:
        number = int(data)
        break
    except Exception:
        print("輸入格式錯誤，請重新輸入")
number = number*2
print(number)
