import os

directory = r"FILL IN DIR FOR PROJECT"
f = open("data.txt", "w")
f.write("")
f.close()
files = os.listdir(directory)
for f in files:
    os.remove(directory+"\\"+f)
