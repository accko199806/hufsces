package hufs.ces.closure

class FiveCards implements Comparable<FiveCards> {

    List<Card> fiveCards = []

    FiveCards(Card[] cards) {
        assert cards.length == 5
        for (int i = 0; i < 5; ++i) {
            fiveCards[i] = cards[i]
        }
        reorder()
    }

    @Override
    int compareTo(FiveCards right) {
        return fiveCards[0] <=> right.fiveCards[0]
    }

    @Override
    String toString() {
        String result = "["
        for (int i = 0; i < 5; ++i) {
            if (i != 0) result += ", "
            result += fiveCards[i].toString()
        }
        result += "]"
        return result
    }

    private void reorder() {
        SelSort sorter = new SelSort()
        fiveCards = sorter.sort(fiveCards, { left, right -> left <=> right })
    }

    def getAt(int i) {
        assert i < fiveCards.size()
        return fiveCards[i]
    }

    List getRank() {
        List temp = []
        for (int i = 0; i < 5; i++) {
            temp.add(fiveCards[i].rank)
        }
        return temp
    }
}
