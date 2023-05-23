import random
number = int(input("put a 4 digit password" ))
guess = 0
tries = 0
while(guess!= number):
    guess = random.randint(0,9999)
    tries = tries +1
    print(guess)
print("your password is????: ",str(number))
print("total comparisions", str(tries))
