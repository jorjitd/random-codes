list = []
def decimalToBinary(x):
    if x > 1:
        decimalToBinary(x // 2)
        list.append(x % 2)
        print(list)

number = int(input("Enter any decimal number: "))

decimalToBinary(number)
