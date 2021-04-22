# Project 1 : Table Display With Bootstrap

### 내용
https://github.com/chomskim/Web-Programming/tree/master/WP2020/StockProject/StockPriceTable 에 있는 프로그램을 수정해 새로운 형식의 Table을 보여주는 Static Web Site를 만든다   
1. stock-table.png 형태를 bootstrap을 이용해 만든다(StockPriceQuery의 static 참조).   
2. Table Head Line은 고정, Line No 추가   
3. Table body는 각 Row가 홀수 짝수로 색이 약간 차이남   
4. Table body는 Scroll 가능   
5. 주식 종목 선정은 자신의 학번 20xx-0yyzz의 xx,yy,zz를 이용해 3가지 종목 선정(네이버, 카카오 고정)   
   숫자 0~29 중 하나 선정(30이상인 경우 30으로 나눈 나머지)   
6. my-style.css추가

<hr>

### 문제 해결 방향
교수님이 만드신 html의 테이블 부분 디자인을 수정하는 게 목표임.   
`table` 클래스에 `table table-striped table-condensed header-fixed` 값을 추가한 후, `my-style.css`를 추가함.

<hr>

### stock-table.png
<img src="https://raw.githubusercontent.com/accko199806/hufsces/master/Web%20Programming%20(CSKim)/report/TableDisplayWithBootstrap/stock-table.png" width="512" />