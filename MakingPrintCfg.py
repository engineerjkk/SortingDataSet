import os

file_path = './data/img/'
file_names = os.listdir(file_path)
print(file_names)

for name in file_names:
    if "jpg" in name:
        print("/data/img/" + name)
print("Finished")