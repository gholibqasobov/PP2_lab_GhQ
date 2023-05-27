word = input()


def palindrome(word):
    temp = list(word)
    temp.reverse()
    temp = "".join(temp)

    if word == temp:
        print(True)
    else:
        print(False)


palindrome(word)