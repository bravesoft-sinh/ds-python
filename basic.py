def user_input():
    name = input("Input your name: ")
    print("Hello " + name)


def conditional(n):
    if n % 2 == 0:
        print("Odd number")
    else:
        print("event number")


def while_loop(n):
    i = 0
    while i < n:
        print(i)
        i = i + 1


def tuples():
    coordinate = (4, 5)
    print(coordinate[0])
    print(coordinate[1])


def dictionary():
    countries = {
        "VN": "Viet Nam",
        "JP": "Japan",
        "US": "America"
    }
    print(countries)
    for key in countries:
        print(countries[key])

    print(countries.get("VN"))


def for_loop(n):
    count = 0
    for i in range(0, n):
        count += 1

    print(count)


def matrix():
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [0]
    ]
    print(mat)
    print(mat[1])
    print(mat[0][2])


matrix()
user_input()
conditional(10)
tuples()
dictionary()
for_loop(10)
while_loop(10)