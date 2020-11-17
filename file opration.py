from pathlib import Path

home = Path.cwd().home()

for file in home.iterdir():
    if file.is_dir():
        print(file,file.is_dir())