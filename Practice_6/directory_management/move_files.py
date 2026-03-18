import shutil
import os

shutil.move("move_files.py", "../move_files.py")

# 2
if not os.path.exists("scripts"): os.mkdir("scripts")
# shutil.move("example.py", "scripts/example.py")

# 3
os.rename("old_name", "new_name")

# 4
for f in os.listdir(): 
    if f.endswith(".txt"): 
        shutil.move(f, "text_folder/")

# 5
shutil.move("source.txt", "dest.txt")