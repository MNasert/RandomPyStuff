import Files.tools as tools


if __name__ == "__main__":

    try:
        file = open("data.dat")
        lines = file.read()
        file.close()
        text = tools.reformat(["<start>", "</start>"], lines)
        print(text)
    except FileNotFoundError:
        print("No such file in directory")

    file = open("data.dat", "a")
    file.write(tools.randomText())
    file.close()

