def slowSort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr) - 1):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]  # pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def mergeSort(arr):
    if len(arr) >= 2:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def selectionSort(arr):
    for i in range(0, len(arr) - 1):
        min_ele_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ele_index]:
                min_ele_index = j

        if min_ele_index != i:
            arr[i], arr[min_ele_index] = arr[min_ele_index], arr[i]

    return arr


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j > 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
