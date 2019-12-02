from random import randint
import time


def gravity_sort(input_list):
    return_list = []
    transposed_list = [0] * max(input_list)
    for num in input_list:
        transposed_list[:num] = [n + 1 for n in transposed_list[:num]]
    for _ in input_list:
        return_list.append(sum(n > 0 for n in transposed_list))
        transposed_list = [n - 1 for n in transposed_list]
    return return_list


l = []
list_size = 100000
for i in range(list_size):
    l.append(randint(1, 11))

print("\nGRAVITY SORT")
start_time = time.time()
gravity_sort(l)
end_time = time.time()

print("Time taken:", end_time - start_time)
print("List Size:", list_size)

print("\nGENERIC SORT")
start_time = time.time()
l.sort()
end_time = time.time()

print("Time taken:", end_time - start_time)
print("List Size:", list_size)
