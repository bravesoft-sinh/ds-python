# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiple(a, b):
    return a * b


def devide(a, b):
    return a / b


# Phương pháp cùi bắp
def sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr) - 1):
            if arr[i] > arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp


def mySort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        mySort(arr, low, pi - 1)
        mySort(arr, pi + 1, high)


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]  # pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array = [1, 2, 4, 6, 8, 3, 9, 4, 3, 5, 7, 4, 8, 9]
    mySort(array, 0, len(array) - 1)
    for element in array:
        print(element)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
