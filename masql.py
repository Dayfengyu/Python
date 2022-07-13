import mysql.connector
# 登入
connection = mysql.connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='880708',
                                     database='sql_tutorial')

cursor = connection.cursor()

# 創建資料庫
# cursor.execute("CREATE DATABASE `qq`;")

# 取得資料庫名稱
# cursor.execute("SHOW DATABASES;")
# records = cursor.fetchall()
# for r in records:
#     print(r)

# 選擇資料庫
# cursor.execute("USE `sql_tutorial`;")

# 創建表格
# cursor.execute("CREATE TABLE `qq`(qq INT);")

# 取得部門表格所有資料
cursor.execute("select * from `branch`;")

# 新增
#cursor.execute("INSERT INTO `branch` VALUES(5,'qq',NULL);")

# 修改
#cursor.execute("UPDATE `branch` SET `manager_id` = 206 WHERE `branch_id` = 4 ;")

# 刪除
#cursor.execute("DELETE FROM `branch` WHERE `branch_id` = 5;")

records = cursor.fetchall()
for r in records:
    print(r)

cursor.close()
connection.commit()
connection.close()
