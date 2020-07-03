# Project 1 : Groovy Array를 이용해서 만드는 전화번호부

### 내용
1. 주어진 PhoneBookProj의 PhoneBookInArray 사용
2. update 함수를 remove, insert로 하지 말고, 직접 찾아 수정하는 것으로 바꿈
3. 번호로부터 이름을 찾아내는 find 함수 완성(테스트데이터 있어야 함)
4. 테스트 케이스 추가 -- insert, remove, update 에 있는 이름, 없는 이름 각각 적용(자신 만의 고유 이름 추가 3명)
5. 2가지 에러 발생하게 함
   
<hr>

### update 함수 수정
```groovy
def update(def name, def num) {
	def entry = find(name);
	if (entry != null) {
		entry.phoneNumber = num
	} else {
		println "***Error -- Name not found";
	}
}
```
기존의 삭제 → 생성 방법과 달리, 이름과 숫자를 입력받고 해당 이름의 값이 존재할 시 번호가 변경되게 수정함.
   
   
### 번호로부터 이름을 찾아내는 find 함수 생성
```groovy
def find(String name){
	for (def i=0; i<lastp; ++i){
		if (arrayPhoneBook[i].phoneName == name)
			return arrayPhoneBook[i];
	}
	return new Entry("not found", -1); // not found
}

def find(int number){
	for (def i=0; i<lastp; ++i){
		if (arrayPhoneBook[i].phoneNumber == number)
			return arrayPhoneBook[i];
	}
	return new Entry("not found", -1); // not found
}
```
`name(String)` `number(Integer)`을 입력받는 find 함수를 만들어 일치하는 Entry가 반환되게 수정함.
