def binary_search(arr, val):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == val:
            return mid
        elif val > arr[mid]:
            low = mid + 1
        elif val < arr[mid]:
            high = mid - 1
    return -1


if __name__ == '__main__':
    li = [12, 15, 17, 19, 21, 24, 45, 67]
    number = 67
    ind = binary_search(li, number)
    print(ind)
