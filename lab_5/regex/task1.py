import re

txt = input()

result = re.search(r'ab*', txt)

if result:
    print("Match found in position", result.start())
else:
    print("No match found")
