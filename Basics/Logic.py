


if __name__ == "__main__":
    argA = True
    argB = False

    if argA and not argB and type(argA) is type(argB) if type(argB) is bool else False:
        print("Wow! A is True; B is False and B is a bool")
    else:
        if type(argB) is not type(argA):
            print("B is no bool")
        else:
            if argB:
                print("B is True!")

    if argA or argB:
        print("A or B is true")