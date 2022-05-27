from Project2MergeSort import merge_sort


def bucket_sort(in_arr):
    out_arr = []
    slot_num = 10

    for i in range(slot_num):
        out_arr.append([])

    for j in in_arr:
        index_a = int(slot_num * j)
        out_arr[index_a].append(j)

    for i in range(slot_num):
        merge_sort(out_arr[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(out_arr[i])):
            in_arr[k] = out_arr[i][j]
            k += 1
    return in_arr


x = [.62, .1, .94, .27, .53, .8]
print(bucket_sort(x))
