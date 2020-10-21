def len(array):
    count = 0;
    for i in array:
        count = count + 1
    return count


def remove(array, index):
    if index < 0 or index >= len(array):
        print("invalid index")
        return []
    new_arr = []
    for i in range(0, len(array)):
        if i != index:
            new_arr.append(array[i])
    return new_arr


array = [1, 2, 3, 4, 5]
print(len(array))
print(remove(array, 10))
