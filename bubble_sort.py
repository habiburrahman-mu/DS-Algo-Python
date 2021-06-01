import random


def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == "__main__":
    A = [random.randint(0, 100) for i in range(20)]
    print(A)
    s = bubbleSort(A)
    print(s)
