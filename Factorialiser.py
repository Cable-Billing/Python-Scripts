import time

try:
    number = int(input("Enter a number "))

    answer = 1

    for i in range(number):
        answer *= i + 1

    print()
    print(str(number) + "! = " + str(answer))

    input()
except:
    print("Not a valid number")
    time.sleep(1.5)
