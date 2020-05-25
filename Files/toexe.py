import random


def reformat(keywordss_t_e, text):
    text = text
    text = text.split(keywordss_t_e[1])
    for i in range(len(text)):
        text[i] = text[i].replace(keywordss_t_e[0], "")
        text[i] = text[i].replace(keywordss_t_e[1], "")
        text[i] = text[i].replace("\n", "")
    return text

def randomText():
    size = random.randint(1, 20)
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"
                , "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    text = "\n<start>\n"
    for i in range(size):
        text += alphabet[random.randint(0, len(alphabet)-1)]
    text += "\n</start>"
    return text


if __name__ == "__main__":

    try:
        file = open("data.dat")
        lines = file.read()
        file.close()
        text = reformat(["<start>", "</start>"], lines)
        print(text)
    except FileNotFoundError:
        print("No such file in directory")

    file = open("data.dat", "a")
    file.write(randomText())
    file.close()
    input("Enter any button to exit... ")