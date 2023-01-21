# Exercise 1
def my_function():
    print("Hello from a function")

# Exercise 2
my_function()

# Exercise 3
def my_second_function(fname, lname):
    print(fname)

# Exercise 4
def func(x):
    return x + 5

# Exercise 5
def my_func(*kids):
    print("The youngest child is " + kids[2])

my_func(*["John", "Collins", "Max"])


# Exercise 6

def my_funct(**kid):
    print("His last name is " + kid["lname"])

kid = {
    "lname": "Jhon",
    "age": 18
}
my_funct(**kid)


# PYTHON LAMBDA FUNCTION

x = lambda a: a
