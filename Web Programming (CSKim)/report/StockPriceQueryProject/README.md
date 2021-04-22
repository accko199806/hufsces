# Project 2 : StockPriceQuery Project 수정

### 내용
2개의 Page home.html(home), list_price_tab.html(listprice)에서 home을 수정(listprice를 참고)    
1. `<textarea></textarea>` 추가(Read Only)   
이수구분:   
학년:   
학번:   
이름:   
2. home에 Session 기능 추가   
3. Submit는 POST로 처리   

<hr>

### 문제 해결 방향
Flask를 이용하여 만들어진 프로그램에서 Session, POST처리를 하는 과제임.   
`webquerystock.py` 파일 내의 home 함수와 `templates/home.html` 파일의 textarea 부분을 수정함.