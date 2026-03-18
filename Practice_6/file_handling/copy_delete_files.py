import shutil
import os

shutil.copy("read_files.py", "read_files_backup.py")

if not os.path.exists("backup_folder"):
    shutil.copytree("../file_handling", "backup_folder")

if os.path.exists("test.txt"):
    os.remove("test.txt")

# 4. Remove empty directory
# os.rmdir("empty_dir")

shutil.move("read_files_backup.py", "archived_script.py")