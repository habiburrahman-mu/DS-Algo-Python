def find_closest_number(arr, target):
    low = 0
    high = len(arr) - 1
    min_diff = float("inf")
    closest_number = None
    # edge cases
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return arr[0]

    while low <= high:
        mid = (low + high) // 2
        # Ensuring that we are not going beyond
        # array ranges
        if mid > 0:
            min_diff_left = abs(arr[mid-1] - target)
        if mid < len(arr) - 1:
            min_diff_right = abs(arr[mid+1] - target)
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_number = arr[mid-1]
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_number = arr[mid + 1]
        # move the mid point according to binary search method
        if target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
        else:  # if the number found on the array
            return arr[mid]
    return closest_number


if __name__ == "__main__":
    A = [1, 2, 5, 7, 9, 11, 14, 15]
    value = 12
    close = find_closest_number(A, value)
    print(close)
