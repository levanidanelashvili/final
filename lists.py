# 1
# nums=[132, 22, 354, 3456, 633]
# print(sum(nums))
# print(max(nums))
# print(min(nums))
# print(sum(nums)/len(nums))
# nums.append((102))
# nums.insert(3, 205)
# nums.pop(4)
# nums.sort()
# print(nums)

# 2
# n=[]
# for i in range(10):
#     x=input("შეიყვანეთ მონაცემი")
#     n.append(x)
# print(n)

# 3
# fruits=["Watermelon", "Apple", "Banana"]
# fruits.sort()
# fruits.reverse()
# print(fruits)

# 4
# def sum(*args):
#     x=1
#     for i in args:
#         x*=i
#     return (x)
# y=sum(1,2,3,4)
# print(y)

# 5
# x=[1, 3, 4, 6, 45, 344, 51, 57, 464, 3432]
# y=[]
# for i in x:
#     if i%2 ==0:
#         y.append(i)
# print(y)

# 6
# x=[1, 3, 4, 6, 45, 344, 51, 57, 464, 3432]
# y=[]
# for i in x:
#     y1=i+10
#     y.append(y1)
# print(y)

# 7
# import random
# x=[]
# for i in range(10):
#     y=random.randint(25,110)
#     x.append(y)
# print(x)
# print(min(x))

# 9
# def list(*num):
#     x=[]
#     for i in num:
#         if i%2==0:
#             x.append(i)
#     print(x)
# x1=list(1,2,3,5465,56,456,)
# print(x1)

# 8
# def funs(x,y):
#     for i in x:
#         if i in y:
#             return True
#     else:
#         return False
# x1=[1,2,3,4]
# x2=[9]
# x3=funs(x1,x2)
# print(x3)

# 10
# f=open("data.txt", "r")
# y=f.read()
# y.strip()
# t=y.split()
# empty = []
# for i in t:
#     if i.__contains__("@"):
#         empty.append(i)
# print(empty)

# 11
# file=open("data_numbers.txt", "r")
# y=file.readlines()
# a=[]
# for i in y:
#     t=int(i)
#     a.append(t)
# print(a)

# 12
# matrix = []
# for i in range(3):
#     a = []
#     for j in range(4):
#         a.append(int(input()))
#     matrix.append(a)
# print(matrix)
# for i in range(3):
#     for j in range(4):
#         print(matrix[i][j]," ")
#     print()

# 13
# import random
#
# x=[1, 3, 5, 7, 4, 33]
# random.shuffle(x)
# print(x)

# 14
# import random
#
# x=[1, 3, 5, 7, 4, 33]
# y=random.choice(x)
# print(y)

# 15
# x=input("input number")
# t=list(x)
# sum=0
# for i in t:
#     y=int(i)
#     sum+=y
# print(sum)

# 16
# x=[1, 5, 23, 5, 12, 2, 5, 1, 18, 5]
# res=[]
# for i in x:
#     y=x.count(i)
#     res.append(y)
# maximum=max(res)
# print("გამეორება",maximum)
# for i in x:
#     if x.count(i)==maximum:break
# print("რიცხვი",i)

# 17
# x=['txt', 'jpg', 'gif', 'html']
# y=input("შეიყვანეთ ნებისმიერი გაფართოება")
# if y in x:
#     print('yes')
# else:
#     print('no')

# 18
# x='python php pascal javascript java c++'
# y=x.split()
# print(y)
# res=[]
# for i in y:
#     t=len(i)
#     res.append(t)
#     lastres=max(res)
# for i in y:
#     if len(i)==lastres:
#         print(i)

# 19
# x=[]
# for i in range(10):
#     y=float(input("input numbers"))
#     x.append(y)
# print('საშუალო',sum(x)/len(x))
# x.sort()
# print(x)
# moda=x[4]+x[5]
# print(moda)
# res=[]
# for i in x:
#     y=x.count(i)
#     res.append(y)
# maximum=max(res)
# if maximum!=1:
#     for i in x:
#         if x.count(i)==maximum:break
#     print("მოდა",i)
# else:
#     print("მოდა არ აქვს")

# 20
# file=open("oscars.txt", "r")
# year=input("input year")
# age=1000
# for each in file:
#     text_split=each.split(",")
#     if text_split[0]==year:
#         print("შეყვანილ წელს ოსკარი მიიღო", text_split[3])
#     min_age=int(text_split[2])
#     if min_age<age:
#         age=min_age
#         youngest=text_split[3]
# print("youngest is", youngest)
# file.close()






























































