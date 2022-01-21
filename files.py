# 1
# f = open('openfile.txt', 'w')
# f.write("hello world its me @@")
# f.close()

# 2
# file= open('openfile.txt', 'r')
# x=file.read()
# print(x)
# special="!@#$%^&*()_+"
# for i in x:
#    if not i.isalnum() and not (i in special): text = x.replace(i, "")
# y=len(text)
# print(y)
# file.close()

# 3
# f=open("openfile.txt", 'a')
# f.write("ok i will do")
# f.close()

# 4
# f=open('data.txt', 'r', encoding='utf8')
# x=f.read()
# print(x)
# file=open('datatext.txt', 'w', encoding='utf8')
# file.write(x)
# f.close()
# file.close()

# 5
# f1=open('data.txt', 'r', encoding='utf8')
# x=f1.read()
# f2=open('openfile.txt', 'r')
# y=f2.read()
# f3=open('f1+f2', 'a', encoding='utf8')
# f3.write(x)
# f3.write(y)
# f1.close()
# f2.close()
# f3.close()

# 6
# f=open('openfile.txt', 'r')
# text=f.read()
# for i in text:
#     if i.islower(): text=text.replace(i, i.upper())
# print(text)
# f.close()

# 7
# file=open('data1.txt', 'w')
# while True:
#     word=input("...")
#     if word=="0":break
#     file.write(word+ '\n')
# file.close()

# 8
# file=open('data1.txt', 'r')
# y=file.read()
# x=""
# for each in y:
#     x+=each.strip().replace("\n", "")
# f=open("data2.txt", "w")
# f.write(x)
# file.closed
# f.closed

# 9
# f=open("data2.txt", "r")
# y=f.read()
# x=y.count("\n")
# x1=y.count(" ")
# x2=x1+x
# if x2==0:
#     print(1)
# else:
#     print(x2)
# special="!@#$%^&*()_+"
# for each in y:
#     if not each.isalnum() and not each in special: y=y.replace(each,"")
# x3=len(y)
# print(x3)



# 10
# f=open('data3.txt', 'w')
# file=open('data4.txt', 'w')
# while True:
#     word=input("...")
#     if word=='0':break
#     f.write(word+'\n')
#     word1=int(word)
#     y=word1**2
#     y1=str(y)
#     file.write(y1+'\n')
# f.close()
# file.close()








































