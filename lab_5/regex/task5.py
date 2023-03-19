import re

txt = input()

result = re.search(r'a.*b\b', txt)

if result:
    print("Match found")
else:
    print("No match")

