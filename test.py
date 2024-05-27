print("Hello World")
num1 = 123
num2 = 456
string1 = "string1"
string2 = "string2"
print(num1 + num2)

# list
list1 = [100, 70, 60, 80, 65]
# 尋找list元素
print(list1[0])
# 添加list元素
list1.append(101)  # 在底部加入
print(list1)
list1.insert(2, 95)  # 在任意位置插入
print(list1)
# 刪除list元素
list1.pop()  # 刪除最後一個元素並返回該值
list1.remove(80)  # 在其中刪除
print(list1)

# dictionary
dict1 = {"AWS": 100, "LINUX": 80, "WIRESHARK": 90}
print(dict1)  # 查詢
dict1["Math"] = 70  # 添加
dict1["Math"] = 60  # 更新18
del dict1["Math"]  # 刪除
print(dict1)

# 用for loop 操作list


# 用for loop 搭配 if else，對list內的元素作判斷

for i in range(len(list1)):
    for j in range(i + 1):
        if list1[j] < list1[i]:
            list1[j], list1[i] = list1[i], list1[j]
        else:
            pass
print(list1)

