def insertion_sort(arr):
    for i in range(1, len(arr)):
        cur_num = arr[i]
        j = i - 1
        while j >= 0 and cur_num < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = cur_num
    return arr


if __name__ == '__main__':
    A = [20, 15, 2, 3, 25, 30, 14, 26, 5, 10, 18, 1]
    s = insertion_sort(A)
    print(s)
