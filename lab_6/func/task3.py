string = input('Enter text: ')
def is_palindrome(string):
    temp = list(string)
    temp.reverse()
    return True if "".join(temp) == string else False


print(is_palindrome(string))
