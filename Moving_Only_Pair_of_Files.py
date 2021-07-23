#선 조건 : 용량이 0KB TXT 파일은 직접 삭제해주어야 합니다.
#라벨링된 텍스트 파일을 먼저 지정 폴더에 옮긴다.
Source_path = './data/img/'
Destination_path ='./data/DataSet/'

import os
import shutil

n=1
for i in os.listdir(Source_path):
    print(i)
    if 'txt' in i:
        shutil.copyfile(Source_path+i,Destination_path+i)
        print("Passing TxT : "+i)

#텍스트 파일명을 리스트에 담는다.
temp=[]
for i in os.listdir(Destination_path):
    #print(k)
    a = i[:-4]
    temp.append(a)
    print("Listing.. : "+i)

#리스트에 있는 이름명의 이미지만 옮긴다.
for i in os.listdir(Source_path):
    b=i[:-4]
    print(b)
    if b in temp:
        shutil.copyfile(Source_path + i, Destination_path + i)
        print("Passing Img : "+i)

#숫자 정렬시키기
file_path = Destination_path
file_names = os.listdir(file_path)
print(file_names)

i = 1

for name in file_names:
    if 'jpg' in name:
        src = os.path.join(file_path, name)
        dst = str(i) + '.jpg'
        dst = os.path.join(file_path, dst)
        os.rename(src, dst)

    if 'txt' in name:
        src = os.path.join(file_path, name)
        dst = str(i) + '.txt'
        dst = os.path.join(file_path, dst)
        os.rename(src, dst)
        i += 1

print("Finished")

