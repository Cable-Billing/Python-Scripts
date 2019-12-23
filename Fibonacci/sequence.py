import argparse

parser = argparse.ArgumentParser()
parser.add_argument('number', type=int, help='number of times to loop')
args = parser.parse_args()

n = args.number
first = 0
second = 1

print(first)
print(second)

for i in range(n - 2):
    answer = first + second
    print(answer)
    first = second
    second = answer
