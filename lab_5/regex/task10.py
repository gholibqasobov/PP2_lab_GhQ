import re
res = []
txt = input()
result = re.findall('[a-zA-Z][a-z]+', txt)
for word in result:
    res.append(word.lower())

print("_".join(res))

# fromCamelCase