


if __name__ == "__main__":
    print("for between 0 and x")
    for i in range(10):
        print(i)

    print("for between x and y")
    for i in range(10, 20):
        print(i)

    print("for item in list")
    x = [["a"], ["b"], ["c"], ["d"], ["e"]]
    for i in x:
        print(i)

    print("for between 0 and length of list")
    for i in range(len(x)):
        print(i)

    print("for letter in string")
    for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(x)

    i = 0
    print("while loop")
    while i < 10:
        i += 1
        print(i)

    i = 0
    print("do-while loop")
    while True:
        i += 1
        print(i)
        if i > 10:
            break

