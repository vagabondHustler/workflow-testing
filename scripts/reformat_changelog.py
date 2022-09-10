import re
import sys

back_tick = "\n```"
content = sys.argv[-1]
expression = "(?!\*\n)\v(\n)"
pattern = re.compile(expression)
new_content = pattern.sub(back_tick, content)
print(new_content)
