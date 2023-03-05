string = input('Enter text: ')
def is_palindrome(string):
    temp = []
    for i in string:
        temp.append(i)
    temp.reverse()
    return True if "".join(temp) == string else False


print(is_palindrome(string))