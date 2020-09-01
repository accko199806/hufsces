# Project 1 : pgzero를 이용한 Connect four Game

### 내용
1. http://220.67.121.119/games/day2/connect4.html   
https://github.com/chomskim/Web-Game/tree/develop/Web-Game-Day2   
참조 (JavaScript로 작성된 프로그램)
2. Python pgzero 를 이용한 프로그램으로 만들기
   
<hr>

### 문제 해결 방향
JQuery가 사용된 Javascript 파일을 분석함.   
pgzero의 `on_mouse_down(pos)`함수를 이용해 클릭 위치를 확인하였고, `draw()`함수를 이용해 원을 그려주었음.   
마지막으로 `checkWinner(ro, co)`함수를 생성해 이긴 사람을 분석하여 게임을 종료함. 
  
<hr>

### 결과
![ss_connect4_image](https://raw.githubusercontent.com/accko199806/hufsces/master/Open%20Source%20SW%20%26%20Experiments%20(CSKim)/report/ConnectFourGame/ss_connect4.png)