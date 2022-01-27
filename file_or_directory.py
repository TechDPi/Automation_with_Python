import os

#Insert the path of the directory inside
dir = ".."

for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.paht.isdir(fullname):
        print(f"{fullname} is a directory")
    else:
        print(f"{fullname} is a file")