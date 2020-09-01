# Project 5 : Raspberry PI 상태 Publish를 받아(Subscribe) MySQL Table에 저장

### 내용
1. https://github.com/chomskim/OSS/tree/master 사용
2. pip install mysql-connector
3. IOT-Proj/sub_mysql.py 수정
4. 4번과제의 프로그램을 pub_stat.py로 고쳐 실행
5. RPi의 같은 폴더에서 dbconfig.py, dbhelper.py, mqconfig.py 와 함께 실행 
6. 4번 과제에서 받은   
   2020-05-29 15:58:08.742108,52.1,27.4,874.5,258.7   
   의 한 Row를   
   temp_time(2020-05-29 15:58:08.742108), temp_data("52.1,27.4,874.5,258.7")   
   두 column으로 저장(MySQL Table은 바꾸지 않는다) 
   
<hr>

### 문제 해결 방향
- report4에서 Publish한 데이터를 Subscribe한 뒤 라즈베리파이에 설치된 MySQL DB에 저장해야 함.   
- pub_stat.py 파일은 report4에서 사용한 파일 그대로 사용해도 됨.
- Publish에서 데이터를 , 간격으로 보냈기 때문에 , 를 기준으로 split 하였고, 10개의 평균을 구해 MySQL DB에 넣었음.
- MySQL 설정과 관련된 부분은 조교님 강의자료에 자세히 나와 있음.