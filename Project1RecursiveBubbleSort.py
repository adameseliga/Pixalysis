import random


def bubble_tool(arr, n):
    if n < 0:
        return arr

    current_array = bubble_tool(arr, n - 1)

    if n < (len(arr) - 1):
        if current_array[n] > current_array[n + 1]:
            temp = current_array[n + 1]
            current_array[n + 1] = current_array[n]
            current_array[n] = temp
            return current_array
        return current_array

    return current_array

def bubble_sort(arr):
    for i in range((len(arr)**2)+1):
            bubble_tool(arr, i)

my_list = []

for x in range(9):
    x = random.randint(0, 101)
    my_list.append(x)

print(my_list)
bubble_sort(my_list)
print(my_list)

if __name__ == '__main__':
    print(__name__)
