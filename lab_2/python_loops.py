# Exersice 1
i = 1
while i < 6:
    print(i)
    i +=1

# Exersice 2

i = 1
while i < 6:
    if i == 3:
        break
    i += 1

# Exercise 3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Exercise 4

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")





# FOR LOOPS


# Exercise 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Exercise 2
for x in fruits:
    if x == "banana":
        continue
    print(x)


# Exercise 3
for x in range(6):
    print(x)


# Exercise 4

for x in fruits:
    if x == "banana":
        break
    print(x)