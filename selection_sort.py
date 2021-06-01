def selectionSort(arr):
    for i in range(len(arr)-1):
        minIndex =0
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if minIndex != i:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]


if __name__ == "__main__":
    A = [20, 15, 2, 3, 25, 30, 14, 26, 5, 10, 18, 1]
    s = selectionSort(A)
    print(s)