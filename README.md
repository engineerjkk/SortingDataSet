# SortingDataSet
![image](https://user-images.githubusercontent.com/76835313/126754159-d7acc385-7134-45d2-afb8-b56c666e48ee.png)
본인의 경로에 맞게 여기 부분만 수정해 줍니다.   
* Source_path : 정렬안된 데이터가 있는 이미지 파일 폴더
* Destination_path : 정렬된 파일을 담을 파일 폴더(미리 만들어주어야 한다.)
## Input : 정렬안된 데이터 셋(이미지와 라벨링된 txt파일이 뒤죽박죽 섞여있다.)
* **라벨링이 되지않은 이미지는 제거한다.**

![image](https://user-images.githubusercontent.com/76835313/126753661-1037c57b-0d11-49c8-8445-f768b84609ab.png)
## Output : 정렬된 데이터 셋
![image](https://user-images.githubusercontent.com/76835313/126753728-c2d7f32f-1358-4a53-aa72-6c4506eb9c67.png)
## Output 2 : 학습시키기 위해 이름 재변경(정확한 sorting을 위해 앞에 0을 붙여준다.) 
[MakingSotring](https://github.com/engineerjkk/SortingDataSet/blob/main/MakingtrainTxT.py)
## Output 3 : cfg 파일을 만들기 위해서 print한다. 이부분을 복사해 yolo-obj.cfg 파일에 넣는다.
https://github.com/engineerjkk/SortingDataSet/blob/main/MakingPrintCfg.py
