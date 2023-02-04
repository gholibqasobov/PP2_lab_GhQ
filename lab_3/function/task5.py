word = input()


def permute(word, l, r):
    if l == r:
        print("".join(word))
    else:
        for i in range(l, r):
            word[l], word[i] = word[i], word[l]
            permute(word, l + 1, r)
            word[l], word[i] = word[i], word[l]


permute(list(word), 0, len(word))
