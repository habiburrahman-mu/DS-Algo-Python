import random


def merge_two_sorted_list(a, b):
    len_a = len(a)
    len_b = len(b)
    sorted_list = []
    i = j = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1

    return sorted_list


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge_two_sorted_list(left, right)


if __name__ == "__main__":
    # a = [5, 8, 12, 56, 70]
    # b = [7, 8, 10, 12, 9, 45, 51]
    # print(merge_two_sorted_list(a, b))

    A = [random.randint(0, 100) for i in range(20)]
    print(A)
    sort = mergeSort(A)
    print(sort)
