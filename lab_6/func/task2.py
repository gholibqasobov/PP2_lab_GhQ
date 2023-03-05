string = input('Enter a string: ')


def upper_lower_count(s):
    lower = upper = 0
    for letter in string:
        if letter.islower():
            lower += 1
        elif letter.isupper():
            upper += 1

    return f'Lower: {lower}, Upper: {upper}'


print(upper_lower_count(string))