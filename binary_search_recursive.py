def binary_search_recursive(arr, value, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    mid_val = arr[mid]
    if mid_val == value:
        return mid
    if value > mid_val:
        left = mid + 1
    else:
        right = mid - 1
    return binary_search_recursive(arr, value, left, right)


if __name__ == "__main__":
    li = [12, 15, 17, 19, 21, 24, 45, 67]
    number = 88
    ind = binary_search_recursive(li, number, 0, len(li)-1)
    print(ind)
