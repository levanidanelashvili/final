import random
def number():
     x = random.randrange(0,101,24)
     return x
sum=0
for i in range(10):
    x=number()
    sum+=x
print("ჯამია", sum)