# Project 4 : MQTT로 Raspberry PI 상태 Publish

### 내용
1. https://github.com/chomskim/OSS/tree/master 사용
2. IOT-Proj/pub_temp.py 수정
3. $ top -n1 을 이용해 컴퓨터 상태 정보를 얻는다. 그 중   
%Cpu(s): 18.8 us,  5.9 sy,-->18.8+5.9(cpu 사용율%)
MiB Mem :    874.5 total, 285.7 used-->874.5와 258.7
4. 현재 (시간, CPU 온도) -- 2020-05-29 15:58:08.742108,52.1
5. 수정 후 (시간, CPU온도, CPU 로드(%), 천체 Mem, 사용 Mem) -- 2020-05-29 15:58:08.742108,52.1,27.4,874.5,258.7
6. $ top -n1 명령 후 나온 text를 분석하는 대신 psutil  이라는 모듈을 (pip install psutil)을 이용해 필요한 정보를 얻어도 됨.(편한 방법 사용, 단 결과는 같아야 함) 
   
<hr>

### 문제 해결 방향
- 문제 설명만 보면 어떤 과제인지 이해하기 힘든데, **현재 시각, CPU 온도, CPU 사용량(%), 전체 메모리, 메모리 사용량**을 MQTT를 통해 Publish 하는 작업임.   
- IOT-Proj/pub_temp.py를 보면 기본적으로 현재 시각과 CPU 온도에 대한 정보를 제공함.   
- 나머지 정보인 CPU 사용량, 전체 메모리, 메모리 사용량은 psutil 라이브러리를 이용하여 구현하였음.   
(`psutil.cpu_percent`, `psutil.virtual_memory().total`, `psutil.virtual_memory().used`)