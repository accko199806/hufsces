# Project 3 : Groovy Sort Program(FiveCards)

### 내용
1. GroovySort를 수정
2. SortTest5Cards에서는 FiveCards의 reorder 후 사전식 순서로 sort
3. FiveCards는 자동으로 reorder되므로 신경쓰지 않아도 됨.
4. Suit(CL, DI, HE, SP)를 고려하지 않고 Rank만을 비교함.
   
<hr>

### Comparator 수정
```groovy
public int compare(FiveCards left, FiveCards right) {
	int comp = 0;
	for(int i = 0; i < 5; i++) {
		int leftStr = left[i].toString().replace("CL", "").replace("DI", "").replace("HE", "")
                    .replace("SP", "").replace("A", "14").replace("J", "11").replace("Q", "12")
                    .replace("K", "13").replace("-", "").replace(",", "").replace(" ", "").toInteger()
        int rightStr = right.fiveCards[i].toString().replace("CL", "").replace("DI", "").replace("HE", "")
                    .replace("SP", "").replace("A", "14").replace("J", "11").replace("Q", "12")
                    .replace("K", "13").replace("-", "").replace(",", "").replace(" ", "").toInteger()
        comp += leftStr - rightStr;
		if (comp != 0) return comp;
	}
	return comp;
}
```
문제에 대한 이해가 부족하여 Suit 값을 모두 Replace한 후 Rank 값만을 추출해 계산하였음.   
FiveCards.groovy의 getAt 함수를 이용하여 정렬하는 방법은 Report#4의 Closure 부분에 있음.
  
<hr>

### 출력 데이터
```
1 [CL-2 , DI-2 , CL-4 , CL-5 , CL-A ]
2 [SP-2 , CL-2 , SP-9 , HE-Q , DI-K ]
3 [CL-2 , HE-3 , CL-3 , SP-7 , SP-10]
4 [DI-2 , HE-3 , SP-4 , CL-5 , CL-A ]
5 [CL-2 , CL-3 , CL-4 , CL-5 , CL-A ]
6 [CL-2 , CL-3 , CL-4 , CL-6 , CL-A ]
7 [DI-2 , SP-3 , HE-5 , DI-6 , DI-Q ]
8 [DI-2 , HE-3 , HE-5 , DI-6 , HE-K ]
9 [HE-2 , CL-3 , DI-6 , HE-8 , CL-J ]
10 [SP-2 , SP-3 , SP-6 , DI-8 , CL-J ]

...
```