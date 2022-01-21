# 3
# text= str(input("text"))
# lenght=len(text)
# print(lenght)

# 4
# text1= str(input("text"))
# text2= str(input("text"))
# x= text1 + text2
# print(x)

# 5
# text4= str(input("text"))
# x=text4.upper()
# print(x)

# 6
# text5= str(input("text"))
# x=text5.count("a")
# print(x)

# 8
# text="სწავლის ძირი მწარე არის, კენწეროში გატკბილდების"
# x= text[:20]
# print(x)
# x1=text.count("ს")
# print(x1)

# 9
# text="Hello WoRld Its Me"
# for i in text:
#     if i.islower(): text=text.replace(i, i.upper())
#     elif i.isupper(): text=text.replace(i, i.lower())
# print(text)

# 10
# text="Hello, this is example of string. Please, write this text and do some exercises"
# x=text.replace("is", "were")

# 11
# text="Hello, this is example of string. Please, write this text and do some exercises"
# lenght=text.strip().count(" ")+1
# print(lenght)


# 12
# text="have a nice day"
# index=14
# while index<=len(text) and index>=0:
#     letter=text[index]
#     print(letter)
#     index-=1

# 17
# name=str(input("name"))
# surname=str(input("surname"))
# x=name+"."+surname+"@btu.edu.ge"
# print(x)

# 14
# x="237645"
# y=len(x)
# print(y)

# 16
# x="levani.danelashvili.1@btu.edu.ge"
# y=x.find("@")
# print(y)

# 13
# text=input("...")
# text1="aeiouAEIOU"
# x=0
# for i in text:
#     if i in text1:
#         x+=1
# print(x)


# 18
# text=input("...")
# digit=0
# upper=0
# lower=0
# special=0
# specialtext="!@#$%^&*()_+"
# for i in text:
#     if i.isdigit(): digit+=1
#     elif i.islower(): lower+=1
#     elif i.isupper(): upper+=1
#     elif i in specialtext: special+=1
# print(digit,upper,lower,special)


# 19
# password=input("password")
# lower=False
# digit=False
# upper=False
# special=False
# specialtext="!@#$%^&*()_+"
# if len(password)>=8:
#     for i in password:
#         if i.islower(): lower=True
#         elif i.isupper(): upper=True
#         elif i.isdigit(): digit=True
#         elif i in specialtext: special=True
# if lower and digit and upper and special:
#     print("პაროლი ვარგისია")
# else:
#     print("თავიდან შეიყვანეთ პაროლი")

# 20
# text=input("...")
# for i in text:
#     if not i.isalpha(): text = text.replace(i,"")
# print(text)

# 22
# text=input("...")
# for i in text:
#     if not i.isalpha(): text = text.replace(i, "")
# word=text
# reverse=text[::-1]
# if word==reverse:
#     print("პოლინდრომია")
# else:
#     print("არაა პოლინდრომი")































