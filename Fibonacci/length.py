import argparse

parser = argparse.ArgumentParser()
parser.add_argument('number', type=int, help='number of times to loop')
args = parser.parse_args()

n = args.number
file = open("data.txt", "w")

first = 0
second = 1

file.write(str(len(str(first))) + "\n")
file.write(str(len(str(second))) + "\n")

for i in range(n - 2):
    answer = first + second
    file.write(str(len(str(answer))) + "\n")
    first = second
    second = answer

file.close()
