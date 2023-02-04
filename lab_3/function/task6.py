word = input()


def rev(word):
    word = list(word.split(" "))
    word.reverse()
    return " ".join(word)

# print(rev(word))
