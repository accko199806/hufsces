# Project 6 : Raspberry PI 상태 Publish를 받아(Subscribe) MySQL Table에 저장하는 동시에 웹으로 상태 그래프 보여주기

### 내용
1. https://github.com/chomskim/OSS/tree/master 사용
2. pip install flask
3. IOT-Web 의 필요 파일 수정
4. MQTT pub/sub는 과제 5와 같음. 단 sub_mysql은 웹서버에서 실행해도 됨 
5. 디스플레이 레코드 수를 20개로 수정
6. 자신의 IOT_Web folder를 Zip하여 제출
7. Chrome에 디스플레이 되는 그래프 동영상 5초 정도 캡쳐해 함께 제출
   
<hr>

### 문제 해결 방향
- Python 기반 웹서버인 Flask를 이용하여 실시간으로 등록되는 MySQL 데이터를 표시하는 과제임.
- pub_stat.py와 sub_mysql.py 파일은 report4, report5에서 사용된 파일을 그대로 사용해도 됨.
- 그래프에 들어가는 항목은 CPU 온도, CPU 사용량, 메모리 사용량 세 개로 메모리는 전체 메모리 / 사용 메모리를 통해 %로 나타내면 됨.
- 디스플레이 레코드 수는 home.html의 script에서 num 값을 20으로 수정하면 됨.
- 라즈베리파이에서 pub sub 작업을 통해 값을 실시간으로 MySQL DB에 넣었으며, 개인용 컴퓨터에서 라즈베리파이의 DB를 연결하고 웹서버를 실행하였음.

<hr>

<img src="https://raw.githubusercontent.com/accko199806/hufsces/master/Open%20Source%20SW%20%26%20Experiments%20(CSKim)/report/RaspStatusShowWeb/diagram.png" width="512" />
[실행 영상](https://github.com/accko199806/hufsces/blob/master/Open%20Source%20SW%20&%20Experiments%20(CSKim)/report/RaspStatusShowWeb/displayVideo.mp4?raw=true)