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

def quicksort(arr):
    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array = [1, 2, 4, 6, 8, 3, 9]
    sort(array)
    for element in array:
        print(element)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


