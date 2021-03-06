# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from sort import quickSort, mergeSort, selectionSort
from util import printList


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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # quicksort
    array = [1, 2, 4, 6, 8, 3, 9, 4, 3, 5, 7, 4, 8, 9]
    print("Given array is", end="\n")
    printList(array)
    quickSort(array, 0, len(array) - 1)
    print("Sorted array is: ", end="\n")
    printList(array)

    # merge sort
    array = [1, 2, 4, 6, 8, 3, 9, 4, 3, 5, 7, 4, 8, 9]
    print("Given array is", end="\n")
    printList(array)
    mergeSort(array)
    print("Sorted array is: ", end="\n")
    printList(array)

    # selection sort
    array = [1, 2, 4, 6, 8, 3, 9, 4, 3, 5, 7, 4, 8, 9]
    print("Given array is", end="\n")
    printList(array)
    selectionSort(array)
    print("Sorted array is: ", end="\n")
    printList(array)

    # insertion sort
    array = [1, 2, 4, 6, 8, 3, 9, 4, 3, 5, 7, 4, 8, 9]
    print("Given array is", end="\n")
    printList(array)
    selectionSort(array)
    print("Sorted array is: ", end="\n")
    printList(array)
