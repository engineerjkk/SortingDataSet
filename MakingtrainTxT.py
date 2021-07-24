import os

file_path = './data/img/'
file_names = os.listdir(file_path)
print(file_names)

i = 1
for name in file_names:
    if 'jpg' in name:
        src = os.path.join(file_path, name)
        if (i < 10):
            dst = '000' + str(i) + '.jpg'
        elif (i < 100):
            dst = '00' + str(i) + '.jpg'
        elif (i < 1000):
            dst = '0' + str(i) + '.jpg'
        else:
            dst = str(i) + '.jpg'
        dst = os.path.join(file_path, dst)
        os.rename(src, dst)
    if 'txt' in name:
        src = os.path.join(file_path, name)
        if (i < 10):
            dst = '000' + str(i) + '.txt'
        elif (i < 100):
            dst = '00' + str(i) + '.txt'
        elif (i < 1000):
            dst = '0' + str(i) + '.txt'
        else:
            dst = str(i) + '.txt'
        dst = os.path.join(file_path, dst)
        os.rename(src, dst)
        i += 1


print("Finished")