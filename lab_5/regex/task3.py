import re

txt = input()

result = re.search('[a-z]+_[a-z]+', txt)

if result:
    print("Sequence:", result.group(), "found in position", result.start())
else:
    print("Sequence match not found")
