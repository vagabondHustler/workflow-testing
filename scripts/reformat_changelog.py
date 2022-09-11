import os
import re
import sys

cwd = os.getcwd()
back_tick = "\\n\\n```\\n\\n"
file_path = f"{cwd}\\changelog.md"

with open(file_path, "r+", encoding="utf-8") as f:
    file_content = f.read()
    expression = "(\\n\\n)"
    pattern = re.compile(expression)
    new_content = pattern.sub(back_tick, file_content)
    f.seek(0)
    f.truncate()
    f.write(new_content)