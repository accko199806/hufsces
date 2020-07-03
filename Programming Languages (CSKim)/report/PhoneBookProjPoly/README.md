# Project 2 : PhoneClassProj를 수정

#### Polymorphism 이 되는 PhoneBook Test를 보여줌

### 내용
1. IPhoneBook interface에 새로운 find 추가
2. PhoneBookArray, PhoneBookList, PhoneBookMap 에 위의 find를 구현
3. PhoneBookArray, PhoneBookList 에 update 수정(과제 1처럼)
4. project#1의 데이터 그대로 테스트 데이터로 사용(2가지 에러), find(number) 테스트 데이터 추가

<hr >

### IPhoneBook interface를 implements한 클래스에 find 함수 추가
#### PhoneBookArray.groovy   

```groovy
@Override
int find(String name) {
    int loc = findLoc(name)
    if (loc == -1) return -1; // not found
    return arrayPhoneBook[loc].phoneNumber
}
    
@Override
String find(int number) {
    for (int i = 0; i < lastp; ++i) {
        if (arrayPhoneBook[i].phoneNumber == number)
            return arrayPhoneBook[i].phoneName
    }
    return "not found"; // not found
}
```

#### PhoneBookList.groovy   

```groovy
@Override
int find(String name) {
    int loc = findLoc(name)
    if (loc == -1)
        return -1; // not found
    return phoneBookList[loc].phoneNumber
}

@Override
String find(int number) {
    for (int i = 0; i < phoneBookList.size(); ++i) {
        if (phoneBookList[i].phoneNumber == number)
            return phoneBookList[i].phoneName
    }
    return "not found"; // not found
}
```

#### PhoneBookMap.groovy

```groovy
@Override
int find(String name) {
    Integer pnumber = phoneBookMap[name]
    if (pnumber != null) {
        return pnumber
    } else {
        return -1
    }
}

@Override
String find(int number) {
    String temp = "not found"
    for (Map.Entry<Integer, String> entry : phoneBookMap.entrySet()) {
        if (entry.getValue() == number) temp = entry.getKey()
    }
    return temp
}
```

interface를 implement 했기 때문에 함수를 재정의(Override) 한 후 name, number 함수를 생성해 값이 반환될 수 있도록 구현함.

### IPhoneBook interface를 implements한 클래스에 find 함수 추가
#### PhoneBookArray.groovy   

```groovy
@Override
boolean update(String name, int number) {
    def loc = findLoc(name)
    if (loc != -1) { // location을 불러와서 번호를 변경시킴.
        arrayPhoneBook[loc].phoneNumber = number
        return true
    } else {
        println "***Error -- Name not found"
        return false
    }
}
```

#### PhoneBookList.groovy

```groovy
@Override
boolean update(String name, int number) {
    def loc = findLoc(name)
    if (loc != -1) { // location을 불러와서 번호를 변경시킴.
        phoneBookList[loc].phoneNumber = number
        return true
    } else {
        println "***Error -- Name not found"
        return false
    }
}

```

#### PhoneBookMap.groovy

```groovy
@Override
boolean update(String name, int number) {
    if (find(name) != -1) {
        phoneBookMap[name] = number
        return true
    } else {
        return false
    }
}
```

report#1과 마찬가지로 삭제 후 생성하는 방식이 아닌, name, number 값을 받고 유효한 경우에 번호를 변경시킴.