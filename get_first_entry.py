def find(arr, value):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if value > arr[mid]:
            low = mid + 1
        elif value < arr[mid]:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            if arr[mid - 1] != value:
                return mid
            high = mid - 1
    return None

if __name__ == "__main__":
    li = [11, 17, 17, 21, 21, 21, 45, 67]
    number = 21
    ind = find(li, number)
    print(ind)