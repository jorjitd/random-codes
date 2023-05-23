import random
score = 0
for i in range(20):
    a = random.randint(0,12)
    b = random.randint(0,12)
    c = a*b
    ans = int(input("whats %d x %d: " %(a,b)))
    if ans == c:
        print("nice")
        score = score + 1
    else:
        print("loser")
print ("You got %d of them right." %(score))
