import re

source_content = "Hello, my name is John."
pattern = r"my name is (.*)"
match = re.search(pattern, source_content)
if match:
    value = match.group(1)
    print(value)  # Output: John
