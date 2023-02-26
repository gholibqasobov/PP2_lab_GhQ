import re

txt = input()

result = re.search('ab[2-3]?', txt)

if result:
    print("Match found in position", result.start())
else:
    print("No match found")