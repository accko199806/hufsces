# Project 3 : pacman2의 Ghost AI 높이기

### 내용
1. https://github.com/chomskim/OSS/tree/pac-branch/pacman2
2. Ghost AI 수정
3. 4개의 Ghost의 AI(추격방법)를 각각 혹은 몇가지 만들어 협동 작전으로 Player를 잡는다.
4. Player가 사탕을 먹은 상태면 도망가는 Move 
   
<hr>

### 문제 해결 방향
- 2개(moveGhosts, followPlayer)로 이루어진 Ghost의 움직임을 수정하여 Player를 보다 더 똑똑하게 잡아야 함.  
- Ghost의 수가 4개였기 때문에 **플레이어를 무조건 쫓아가는 Ghost** , **플레이어의 가는 방향을 막는 Ghost**, **플레이어의 상단을 쫓아가 탈출구를 막는 Ghost**, **플레이어의 하단을 쫓아가 탈출구를 막는 Ghost**로 구현함.   
- Player의 점수가 3천점이 넘을 시 Ghost의 이동 속도를 3에서 3.2로 증가시킴.
- 사탕의 기본 지속시간을 1200에서 800으로 낮춰 Player가 Ghost를 위협하는 시간을 줄임.
- Player가 사탕을 먹은 경우 Ghost가 Player의 이동 방향에 대해 반대로 이동하게 함.

  
<hr>

### 결과
<img src="https://raw.githubusercontent.com/accko199806/hufsces/master/Open%20Source%20SW%20%26%20Experiments%20(CSKim)/report/Pacman2/ss_pacman2.png" width="512" />