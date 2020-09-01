# Project 2 : pgzero를 이용한 Pong Game

### 내용
1. https://github.com/chomskim/OSS/tree/master/pgzero/pong   
https://github.com/chomskim/OSS/tree/master/ai-pong   
https://github.com/chomskim/Web-Game/blob/develop/Web-Game-Day3/1pong/pong3.html   
참조 (JavaScript로 작성된 프로그램)
2. ai-pong프로그램을 수정
3. pong3의 AI(기존, Left)를 이길 수 있는 새로운 AI(Right) 적용
4. 각도는 벽에 대해 30도 보다 커야 한다.
   
<hr>

### 문제 해결 방향
Pong Game의 경우 문제 해결에 대한 문의가 너무 많아 조교님께서 코드 설명을 다 해주셨음.   
PyGame Zero로 짜여진 Pong Game을 pgzero로 변형한 https://github.com/chomskim/OSS/blob/master/ai-pong/pgz-pong.py 파일을 이용하였음.   
기존 LEFT AI를 복제하여 RIGHT AI를 만들었고, 공의 위치에 대해 패달의 위치가 바뀌도록 코드를 수정하여 무조건 RIGHT AI가 이기도록 설계함. 
  
<hr>

### 결과
<img src="https://raw.githubusercontent.com/accko199806/hufsces/master/Open%20Source%20SW%20%26%20Experiments%20(CSKim)/report/PongGame/ss_pong3.png" width="512" />