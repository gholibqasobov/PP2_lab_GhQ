# Python Intro

# Python Syntax

print("Hello World")

if 5 > 2: # space after explanation mark is important
    print("Five is greater than two!")

# Python Comment

# This is a comment

'''
This is a comment
written in more than just one line
'''

# Python Variables


# Exercise 1
carname = "Volvo"

# Exercise 2
x = 50


# Exercise 3
x = 5
y = 10

print(x + y)

# Exercise 4
x = 5
y = 10
z = x + y
print(z)

# Exercise 5

# 2my-first_name = "John"
my_first_name = "John"


# Exercise 6
x = y = z = "Orange"


# Exercise 7
def myfunc():
    global x
    x = "fantastic"


# Python Data Types

# Exercise 1
x = 5
print(type(x))

# Exercise 2
x = "Hello world"
print(type(x))

# Exercise 3
x = 20.5
print(type(x))

# Exercise 4
x = ["apple", "banana", "cherry"]
print(type(x))

# Exercise 5
x = ("apple", "banana", "cherry")
print(type(x))

# Exercise 6
x = {"name": "John", "age": 36}
print(type(x))

# Exercise 7
x = True
print(type(x))



# Python Numbers

# Exercise 1
x = 5
x = float(x)

# Exercise 2
x = 5.5
x = int(x)

# Exercise 3
x = 5
x = complex(x)


# Python Strings


# Exercise 1
x = "Hello World"
print(len(x))

# Exercise 2
txt = "Hello World"
print(txt[0])


# Exercise 3
txt = "Hello World"
x = txt[2:5]

# Exercise 4
txt = " Hello World "
x = txt.strip()

# Exercise 5
txt = "Hello World"
txt = txt.upper()

# Exercise 6
txt = "Hello World"
txt = txt.lower()

# Exercise 7
txt = "Hello World"
txt = txt.replace("H", "J")

# Exercise 8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# or

print("My name is John, and I am ()".format(age))



# Python Booleans

# Exercise 1
print(10 > 9)
# True

# Exercise 2
print(10 == 9)
# False

# Exercise 3
print(10 < 9)
# False

# Exercise 4
print(bool("abc"))
# True

# Exercise 5
print(bool(0))
# False

# Python Operators

# Exercise 1
print(10 * 5)

# Exercise 2
print(10 / 2)

# Exercise 3

fruits = ["apple", "banana"]

if "apple" in fruits:
    print("Yes, apple is a fruit!")

# Exercise 4
if 5 != 10:
    print("5 and 10 is not equal")

# Exercise 5

if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")

