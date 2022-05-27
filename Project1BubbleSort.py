import random


def bubble_sort(arr):
    for i in arr:
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp


my_array = []

for x in range(9):
    x = random.randint(0, 101)
    my_array.append(x)


print(my_array)
bubble_sort(my_array)
print(my_array)
    

if __name__ == '__main__':
    print(__name__)
