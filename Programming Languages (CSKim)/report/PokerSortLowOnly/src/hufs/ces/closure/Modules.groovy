package hufs.ces.closure

class Modules {

    /** Required Functions **/
    static List filter(List list, Closure comp) {
        if (list.size() == 0) return list
        else {
            if (comp(list.head())) return [list.head()] + filter(list.tail(), comp)
            else filter(list.tail(), comp)
        }
    }

    static List freMove(List list, def num) {
        return filter(list) { it != num }
    }

    static List merge(List L1, List L2, Closure comp) {
        if (L1.size() == 0) return L2
        else if (L2.size() == 0) return L1
        else {
            def x = L1.head()
            def y = L2.head()
            if (comp(x, y) < 0) return [x] + merge(L1.tail(), L2, comp)
            else return [y] + merge(L1, L2.tail(), comp)
        }
    }

    static List mergeSort(List list, Closure comp) {
        def n = list.size()
        if (n <= 1) return list
        else {
            def n2 = (int) n / 2
            def L1 = list[0..n2 - 1]
            def L2 = list[n2..n - 1]
            return merge(mergeSort(L1, comp), mergeSort(L2, comp), comp)
        }
    }

    /** Custom Code **/
    static List getPairs(List list) {
        if (list.size() < 2) return []
        else {
            if (list[0] == list[1]) return [list[0]] + getPairs(list[2..<list.size()])
            else return getPairs(list[1..<list.size()])
        }
    }

    static List getTriple(List list) {
        if (list.size() < 3) return []
        else {
            if (list[0] == list[1] && list[0] == list[2]) return [list[0]]
            else return getTriple(list[1..<list.size()])
        }
    }

    static List getFourCard(List list) {
        if (list.size() < 4) return []
        else {
            if (list[0] == list[1] && list[0] == list[2] && list[0] == list[3]) return [list[0]]
            else return getFourCard(list[1..<list.size()])
        }
    }

    static List setPokerLowOrder(List<FiveCards> list) {
        List<Entry> resultList = []
        list.each {
            List rank = it.getRank()
            List tempList = []
            if (getFourCard(rank).size() != 0) {
                tempList.add(6)  // Add FourCard Indicator
                tempList.add(getFourCard(rank)[0])  // Add FourCard Number
                List RemainNum = freMove(rank, tempList[1])  // Remove FourCard Number
                RemainNum.each { tempList.add(it) }  // Add Remaining Number to List
                resultList.add(new Entry(it, tempList))  // Add TempList to Result List
                return
            }

            if (getTriple(rank).size() != 0) {  // if Triple or FullHouse
                if (getFourCard(rank).size() != 0) return  // if FourCard (Protect Four Card Duplicate)
                Integer TripleNum = getTriple(rank)[0]
                // Assign Number (Distinguished Whether it is FullHouse or Triple)
                List RemainNum = freMove(rank, TripleNum)  // Remove Triple Number
                if (getPairs(RemainNum).size() != 0) {  // if FullHouse
                    tempList.add(5)  // Add FullHouse Indicator
                    tempList.add(TripleNum)  // Add Triple Number
                    tempList.add(getPairs(RemainNum)[0])  // Add Pairs Number
                } else { // if Triple
                    tempList.add(4)  // Add Triple Indicator
                    tempList.add(TripleNum)  // Add Triple Number
                    List RemainSortedNum = mergeSort(RemainNum, { x, y -> (x <=> y) * (-1) })  // Sort Remain Numbers
                    RemainSortedNum.each { tempList.add(it) }  // Add Remaining Number to List
                }
                resultList.add(new Entry(it, tempList))  // Add TempList to Result List
                return
            }

            if (getPairs(rank).size() != 0) {  // if OnePair or TwoPair
                if (getFourCard(rank).size() != 0) return  // if FourCard (Protect Four Card Duplicate)
                if (getTriple(rank).size() != 0) return  // if Triple (Protect Four Card Duplicate)
                if (getPairs(rank).size() == 1) {  // if OnePair
                    tempList.add(2)  // Add OnePair Indicator
                    tempList.add(getPairs(rank)[0])  // Add OnePair Number
                    List RemainSortedNum = mergeSort(freMove(rank, getPairs(rank)[0]), { x, y -> (x <=> y) * (-1) })
                    // Sort Remain Numbers
                    RemainSortedNum.each { tempList.add(it) }  // Add Remaining Number to List
                }
                if (getPairs(rank).size() == 2) {  // if TwoPair
                    tempList.add(3)  // Add TwoPair Indicator
                    List TwoPairSortedNum = mergeSort(getPairs(rank), { x, y -> (x <=> y) * (-1) })
                    // Sort TwoPair Numbers
                    TwoPairSortedNum.each { tempList.add(it) }  // Add TwoPair Number to List
                    List TempList = freMove(rank, TwoPairSortedNum[0])  // Remove TwoPair Number
                    List RemainSortedNum = mergeSort(freMove(TempList, TwoPairSortedNum[1]), { x, y -> (x <=> y) * (-1) })
                    // Sort Remain Numbers
                    RemainSortedNum.each { tempList.add(it) }  // Add Remaining Number to List
                }
                resultList.add(new Entry(it, tempList))  // Add TempList to Result List
                return
            }

            if (getPairs(rank).size() == 0) {  // if NoPair
                tempList.add(1)
                List RemainSortedNum = mergeSort(rank, { x, y -> (x <=> y) * (-1) })
                // Sort Remain Numbers
                RemainSortedNum.each { tempList.add(it) }  // Add Remaining Number to List
                resultList.add(new Entry(it, tempList))  // Add TempList to Result List
                return
            }
        }
        return resultList
    }
}