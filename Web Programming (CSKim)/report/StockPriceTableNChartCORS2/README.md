# Project 4 : StockPriceTableNChartCORS 보완(Report#3에서 시작)

### 내용   
1. Chart와 Table(여러개 나오게 함)을 2개의 Column에 만든다.   
   Responsive로 화면이 줄어들면 1 Column으로 표시   
2. Delete Chart와 Delete Table 기능(마지막 추가 된 Element 삭제) 추가   

<hr>

### 문제 해결 방향
- 과제 3번에서 사용했던 코드를 그대로 이용함.   
- `Grid Display`를 이용하여 반응형을 구현함.   
- Show Chart, Show Table 버튼을 눌렀을 때 Grid 영역에 `div`가 추가되도록 구현하였고, Delete Chart, Delete Table 버튼을 눌렀을 경우 추가된 `div`의 마지막 Element를 삭제하도록 구현함.
- `templates/home.html`, `static/css/index.css` 파일을 수정함.