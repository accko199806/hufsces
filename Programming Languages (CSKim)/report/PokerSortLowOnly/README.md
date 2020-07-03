# Project 5 : Poker Sort Low Only

### 내용
1. GroovySortClosure hufs.ces.sort.closure의 FiveCardsComparator Closure 작성
   -- 주어진 FiveCards를 아래와 같은 List로 만드는 것이 사실 상 어려운 문제임.
2. 다음의 Poker Low Order 규칙 적용   
• Ace는 1로만 생각   
• No Pair(1), One Pair(2), Two Pair(3), Triple(4), Full House(5), Four Card(6) 만 사용   
• 첫자리수는 위 족보의 숫자 다음 자리는 각 경우 따라 추가 자리수(10이 넘을 수도 있음)를 주어 최종 비교(사전순)   
예)   
A,2,3,4,5 --> No Pair(1),(5),(4),(3),(2),(1) --> [1,5,4,3,2,1]   
A,2,3,4,6 --> No Pair(1),(6),(4),(3),(2),(1) --> [1,6,4,3,2,1]   
A,2,3,5,6 --> No Pair(1),(6),(5),(3),(2),(1) --> [1,6,5,3,2,1]   
A,5,7,Q,K --> No Pair(1),(13),(12),(7),(5),(1) --> [1,13,12,7,5,1]   
A,A,2,3,4 --> One Pair(2,1),(4),(3),(2) --> [2,1,4,3,2]   
K,K,6,8,J --> One Pair(2,13),(11),(8),(6) --> [2,13,11,8,6]   
K,K,5,8,Q --> One Pair(2,13),(12),(8),(5) --> [2,13,12,8,5]   
A,A,2,2,3 --> Two Pair(3,2,1),(3) --> [3,2,1,3]   
K,K,Q,Q,J --> Two Pair(3,13,12),(11) --> [3,13,12,11]   
K,K,Q,Q,9 --> Two Pair(3,13,12),(9) --> [3,13,12,9]   
A,A,A,2,3 --> Triple(4,1),(3),(2) --> [4,1,3,2]   
K,K,K,Q,J --> Triple(4,13),(12),(11) --> [4,13,12,11]   
K,K,K,Q,8 --> Triple(4,13),(12),(8) --> [4,13,12,8]   
A,A,A,2,2 --> Full House(5,1,2) --> [5,1,2]   
K,K,K,Q,Q --> Full House(5,13,12) --> [5,13,12]   
K,K,K,J,J --> Full House(5,13,11) --> [5,13,11]   
A,A,A,A,2 --> Four Card(6,1),(2) --> [6,1,2]   
K,K,K,K,Q --> Four Card(6,13),(12) --> [6,13,12]   
K,K,K,K,A --> Four Card(6,13),(1) --> [6,13,1]
   
<hr>

### Modules 구현
```groovy
static List filter(List list, Closure comp)
static List freMove(List list, def num)
static List merge(List L1, List L2, Closure comp)
static List mergeSort(List list, Closure comp)
static List getPairs(List list)
static List getTriple(List list)
static List getFourCard(List list)
static List setPokerLowOrder(List<FiveCards> list)
```
[SP-K, CL-K, HE-A, CL-A, DI-A]와 같은 SortTest5Cards 데이터를 [7, 14, 13]으로 변경하는 과제임.   
hufs.ces.closure 패키지 내에 Moduels.groovy 클래스를 추가하여 위의 기능을 처리할 함수들을 정리함.   
실제 기능이 동작하는 클래스는 SortTest5Cards의 main 함수이며 QuickSort를 통해 Low Order 정렬함.
   
<hr>

### 출력 데이터
```
...

100	 [SP-2, SP-3, CL-9, SP-K, DI-K] 	 -> One Pair : [2, 13, 9, 3, 2]
101	 [DI-A, HE-A, SP-7, DI-7, HE-8] 	 -> Two Pair : [3, 7, 1, 8]
102	 [SP-A, CL-5, HE-5, HE-7, CL-7] 	 -> Two Pair : [3, 7, 5, 1]
103	 [HE-A, SP-A, SP-2, SP-10, HE-10] 	 -> Two Pair : [3, 10, 1, 2]
104	 [CL-A, DI-A, CL-2, SP-10, HE-10] 	 -> Two Pair : [3, 10, 1, 2]
105	 [DI-A, HE-A, CL-A, DI-6, HE-7] 	 -> Triple Pair : [4, 1, 7, 6]
106	 [HE-6, HE-8, DI-8, SP-8, DI-J] 	 -> Triple Pair : [4, 8, 11, 6]
107	 [CL-A, DI-A, HE-A, SP-K, CL-K] 	 -> Full House : [5, 1, 13]
108	 [CL-A, DI-A, HE-A, SP-A, CL-2] 	 -> Four Cards : [6, 1, 2]
```