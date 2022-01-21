# 1
# while True:
#     try:
#         a = int(input("input number"))
#         b = int(input("input number"))
#         c = a / b
#         print("განაყოფია", c)
#         break
#     except ZeroDivisionError as m:
#         print(m)
#     except ValueError as m1:
#         print(m1)
#     except:
#         print("error!")

# 2
# def division(a, b):
#     try:
#         return a/b
#     except ZeroDivisionError as m:
#         return m
#     except ValueError as m1:
#         return m1
#     except:
#         return "error!"
# d = division(3,"3")
# print(d)

# 3
# try:
#     a=[1,3,5,7,3,245,673,2354]
#     index=int(input("input index"))
#     print(a[index])
# except IndexError as m:
#     print(m)
# except ValueError as m1:
#     print(m1)
# except:
#     print("ERROR!")

# 5
# import math
# try:
#     a = float(input("input number"))
#     b = float(input("input number"))
#     c = float(input("input number"))
#     d = b ** 2 - 4 * a * c
#     sqrt1 = math.sqrt(d)
#     x1 = (b ** 2 - sqrt1) / (2 * a)
#     x2 = (b ** 2 + sqrt1) / (2 * a)
#     print(x1, x2)
# except ZeroDivisionError as m:
#     print(m)
# except ValueError as m1:
#     print(m1)
# except TypeError as m2:
#     print(m2)

# 6
# lists = []
# try:
#     a = float(input("input number"))
#     lists.append(a)
#     b = float(input("input number"))
#     lists.append(b)
#     c = float(input("input number"))
#     lists.append(c)
#     maximum=max(lists)
#     lists.remove(maximum)
#     if sum(lists) > maximum:
#         lists.append(maximum)
#         print(sum(lists)/len(lists))
#     else:
#         raise Exception("impossible")
# except Exception as m:
#     print(m)

# 4
# try:
#     file = open("myresult.txt", "r")
#     file.read()
# except Exception as m:
#     print(m)










