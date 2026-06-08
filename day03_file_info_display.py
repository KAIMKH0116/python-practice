import os

folder = "C:/Users/OWNER/OneDrive/Desktop/python-practice"
files = os.listdir(folder)

print(len(files))

for file in files:
    if file.endswith(".py"):
        print(file)