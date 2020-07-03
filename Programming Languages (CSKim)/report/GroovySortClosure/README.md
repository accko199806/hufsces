# Project 4 : Groovy Sort Closure Program(FiveCards)

### 내용
1. GroovySortClosure를 수정
2. 기능은 Project#3와 같고 Comparator Class 대신 compare를 하는 closure를 만든다
   
<hr>

### Closure 구현
```groovy
Closure comp = { left, right ->
        int temp = 0
        for (int i = 0; i < 5; i++) {
            temp = left[i] <=> right[i]
            if (temp != 0) return temp
        }
        return temp
    }
}
```
Project#3와 다르게 Comparator를 이용하지 않고 Closure로 구현하였음.   
`List<FiveCards> list5cardSorted = new QuickSort().sort(list5card, comp)`와 같이 사용됨.
  
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