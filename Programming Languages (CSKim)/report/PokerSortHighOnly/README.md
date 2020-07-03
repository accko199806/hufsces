# Project 6 : Poker Sort High Only

### 내용
1. GroovySortClosure hufs.ces.sort.closure의 FiveCardsComparator Closure 작성
   -- 주어진 FiveCards를 아래와 같은 List로 만드는 것이 사실 상 어려운 문제임.
2. 다음의 Poker High Order 규칙 적용   
• Ace는 1과 14로 생각(1로 생각하는 경우는 1,2,3,4,5 인 Straight 일때 뿐임)   
• No Pair(1), One Pair(2), Two Pair(3), Triple(4), Straight(5), Flush(6), Full House(7), Four Card(8), Straight Flush(9)     
• 첫자리수는 위 족보의 숫자 다음 자리는 각 경우 따라 추가 자리수(10이 넘을 수도 있음)를 주어 최종 비교(사전순)   
예)   
A,2,3,4,6 --> No Pair(1),(14),(6),(4),(3),(2) --> [1,14,6,4,3,2]   
A,2,3,5,6 --> No Pair(1),(14),(6),(5),(3),(2)) --> [1,14,6,5,3,2]   
A,5,7,Q,K --> No Pair(1),(14),(13),(12),(7),(5) --> [1,14,13,12,7,5]   
A,A,2,3,4 --> One Pair(2,14),(4),(3),(2) --> [2,14,4,3,2]   
K,K,6,8,J --> One Pair(2,13),(11),(8),(6) --> [2,13,11,8,6]   
K,K,7,8,J --> One Pair(2,13),(11),(8),(7) --> [2,13,11,8,7]   
A,A,2,2,3 --> Two Pair(3,14,2),(3) --> [3,14,2,3]   
K,K,Q,Q,J --> Two Pair(3,13,12),(11) --> [3,13,12,11]   
K,K,Q,Q,9 --> Two Pair(3,13,12),(9) --> [3,13,12,9]   
A,A,A,2,3 --> Triple(4,14),(3),(2) --> [4,14,3,2]   
K,K,K,Q,J --> Triple(4,13),(12),(11) --> [4,13,12,11]   
K,K,K,Q,8 --> Triple(4,13),(12),(8) --> [4,13,12,8]   
10,J,Q,K,A --> Straight(5),(14) --> [5,14]   
A,2,3,4,5 --> Straight(5),(5) --> [5,5]   
A,2,3,5,6 --> Flush(6),(14),(6),(5),(3),(2)) --> [6,14,6,5,3,2]   
A,A,A,2,2 --> Full House(7,14,2) --> [7,14,2]   
K,K,K,Q,Q --> Full House(7,13,12) --> [7,13,12]   
K,K,K,J,J --> Full House(7,13,11) --> [7,13,11]   
A,A,A,A,2 --> Four Card(8,14),(2) --> [8,14,2]   
K,K,K,K,Q --> Four Card(8,13),(12) --> [8,13,12]   
K,K,K,K,A --> Four Card(8,13),(1) --> [8,13,14]   
A,2,3,4,5 --> Straight Flush(9),(5) --> [9,5]   
10,J,Q,K,A --> Straight Flush(9),(14) --> [9,14]   
   
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
static List getStraight(List list)
static List getFlush(List rank, List suit)
static List getStraightFlush(List rank, List suit)
static List setPokerHighOrder(List<FiveCards> list)
```
[SP-K, CL-K, HE-A, CL-A, DI-A]와 같은 SortTest5Cards 데이터를 [7, 14, 13]의 형태로 변경하는 과제임.   
hufs.ces.closure 패키지 내에 Moduels.groovy 클래스를 추가하여 위의 기능을 처리할 함수들을 정리함.   
실제 기능이 동작하는 클래스는 SortTest5Cards의 main 함수이며 QuickSort를 통해 High Order 정렬함.   
Straight, Flush, StraightFlush 등이 추가되었고, A가 1과 14로 작용되는 등의 기능이 추가됨.
   
<hr>

### 출력 데이터
```
1	 [CL-2, CL-3, CL-4, CL-5, CL-A] 	 -> Straight Flush : [9, 5]
2	 [CL-2, DI-A, HE-A, SP-A, CL-A] 	 -> Four Card : [8, 14, 2]
3	 [SP-K, CL-K, HE-A, CL-A, DI-A] 	 -> Full House : [7, 14, 13]
4	 [CL-2, CL-3, CL-4, CL-6, CL-A] 	 -> Flush : [6, 14]
5	 [CL-7, CL-8, CL-9, HE-10, DI-J] 	 -> Straight : [5, 11]
6	 [DI-2, HE-3, SP-4, CL-5, CL-A] 	 -> Straight : [5, 5]
7	 [DI-6, HE-7, HE-A, DI-A, CL-A] 	 -> Triple : [4, 14, 7, 6]
8	 [HE-6, HE-8, DI-8, SP-8, DI-J] 	 -> Triple : [4, 8, 11, 6]
9	 [SP-2, SP-10, HE-10, HE-A, SP-A] 	 -> Two Pair : [3, 14, 10, 2]
10	 [CL-2, HE-10, SP-10, DI-A, CL-A] 	 -> Two Pair : [3, 14, 10, 2]

...
```