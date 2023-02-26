import re

txt = input()

result = re.search('[A-Z][a-z]+', txt)

if result:
    print("Sequence:", result.group(), "found in position", result.start())
