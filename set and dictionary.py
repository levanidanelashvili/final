# 1
# dic = {0: 10, 1: 20}
# dic[2]=30
# dic[3]=40
# dic.update({4:30, 5:50})
# print(dic)
# dic.pop(0)
# del dic[4]
# print(dic)

# 2
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)

# 3
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key=int(input("input key"))
# t=[]
# for keys in d:
#     t.append(keys)
# if key in t:
#     print(True)
# else:
#     print(False)

# 4
# d = {'x': 10, 'y': 20, 'z': 30}
# for key, value in d.items():
#     print(key, "->", value)

# 5
# keys = list(range(1, 10))
# dic = {}
# for i in keys:
#     t = i**3
#     t1 = str(t)
#     i1 = str(i)
#     r = dic.fromkeys(i1, t1)
#     dic.update(r)
# print(dic)

# 6
# family = {
#     "firstname": "Jane",
#     "lastname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "firstname": "Alice",
#             "age": 6,
#         },
#         {
#             "firstname": "Bob",
#             "age": 8,
#         }
#     ]
# }
# name = family["firstname"]
# lastname = family["lastname"]
# age = family["age"]
# child1 = family["children"][0]["firstname"]
# child2 = family["children"][1]["firstname"]
# print(name, lastname, age, ",", child1, ",", child2)

# 7
# file = open("morsecode.txt", "r")
# lists = []
# for each in file:
#     strip = each.strip("\n")
#     split = strip.split("\t")
#     lists.append(split)
# length = len(lists)
# new_dic = {}
# for i in range(length):
#     kay = lists[i][0]
#     value = lists[i][1]
#     dic = new_dic.fromkeys(kay, value)
#     new_dic.update(dic)
# word = input("input word")
# code = ""
# for each in word:
#     for key in new_dic:
#         if each == key:
#             value = new_dic[key]
#             code += value
#     if each == " ":
#         code += "|"
# print(code)
# file.close()

# 8
# my_set = {0, 1, 2, 3, 4}
# my_set.add(5)
# my_set.update([6, 7])
# my_set.discard(1)
# my_set.remove(0)
# length = len(my_set)
# print("სიგრძეა", length)
# for each in my_set:
#     print(each)

# 9
# set1 = {"green", "blue"}
# set2 = {"blue", "yellow"}
# c = set1.union(set2)
# d = set1 | set2
# print(c, d)
#
# c1 = set1.difference(set2)
# d1 = set1 - set2
# print(c1, d1)
#
# c2 = set1.intersection(set2)
# d2 = set1 & set2
# print(c2, d2)
#
# c3 = set1.symmetric_difference(set2)
# d3 = set1 ^ set2
# print(c3, d3)

# 10
# my_set = {1, 2, 3, 546, 456, 234, 23, 2134, 4, 23, 324}
# print("max", max(my_set), "min", min(my_set))

# 11
# text = input("input words")
# my_set = set(text)
# for each in my_set:
#     print(each)

# 12
# text1 = set(input("input word"))
# text2 = set(input("input word"))
# my_set = text1.intersection(text2)
# print(my_set)


