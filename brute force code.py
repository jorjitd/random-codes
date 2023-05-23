import random




x = int(input("pick a 4 digit password?: "))
print("i will now guess your secret password")


for num in range(1000):
    print(random.randint(1, 9999))

print("is this your password?")

print(x)
