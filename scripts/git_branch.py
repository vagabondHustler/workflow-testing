import subprocess
from datetime import datetime

dt = datetime.now()
date_time = int(dt.strftime("%y%m%d%H%M%S"))

menu = f"""
1.    new feature branch:        feat/{date_time}
2.    new fix branch:            fix/{date_time}
3.    new chore branch:          chore/{date_time}
4.    new tests branch:          test/{date_time}
"""

print(menu)
output = input("Select new branch to create from main: ")
if output == "1":
    subprocess.Popen(f"git checkout -b feat/{date_time} main")
elif output == "2":
    subprocess.Popen(f"git checkout -b fix/{date_time} main")
elif output == "3":
    subprocess.Popen(f"git checkout -b chore/{date_time} main")
elif output == "4":
    subprocess.Popen(f"git checkout -b test/{date_time} main")
