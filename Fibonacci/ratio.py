import time

try:
    n = int(input("Pick a number... "))

    first = 0
    second = 1

    for i in range(n):
        answer = first + second
        first = second
        second = answer
        print(str(i + 1) + ": " + str(second / first))

    print()
    input("Press enter to exit...")
except:
    print("That was not a number")
    time.sleep(1.5)
