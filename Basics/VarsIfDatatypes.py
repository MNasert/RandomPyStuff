



if __name__ == "__main__":
    integer = 2
    print(integer, type(integer))

    flo = 3.1415
    print(flo, type(flo))

    boolean = False
    print(boolean, type(boolean))

    lis = [0, 1, 2, 3]
    print(lis, type(lis))

    mulLis = [[["a"], ["b"], ["c"]], [["d"], ["e"], ["f"]]]
    print(mulLis, type(mulLis))

    string = "imma mafakin string bitch"
    print(string, type(string), "\n")
    ###
    ###
    ###
    ###
    ###
    ###
    ###
    ###
    ###
    ###
    ###
    ###
    ###
    ###
    ###
    if type(integer) is int:
        print("Wow", integer, "is an integer")

    if type(flo) is float:
        print("Wow", flo, "is a float", "\n")
    ###
    ###
    ###
    ###
    ###
    ###
    ###
    ###
    ###
    if flo > integer:
        print("wow", flo, "is greater", integer)
    else:
        print("Wow", integer, "is greater", flo)

    if integer > flo:
        print("wow", integer, "is greater", flo)
    else:
        print("whooops", integer, "is smaller", flo, "\n")
    ###
    ###
    ###
    ###
    ###
    ###
    ###
    ###
    ###
    ###
    ##
    if len("me") > len("you"):
        print("this shouldn´t happen")
    elif "True" == "True":
        print("True is True")

    if boolean:
        print("TRUEEE")
    elif not boolean:
        print("NO TRUEEEE")
