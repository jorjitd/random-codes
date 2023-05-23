import random
a = str(input("first name?: "))
b = str(input("second name?: "))
c = a[:3] +b[-2:] +str(random.randint(100,999))
print(c)
