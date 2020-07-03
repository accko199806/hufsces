package hufs.ces.closure

class SortTest5Cards {

    static final int CLUB = 1, DIAMOND = 2, HEART = 3, SPADE = 4

    static List<FiveCards> generate5CardList(int genCount) {
        List<FiveCards> p5CardsList = []
        List<Card> deckCard = []

        for (int s = Card.CLUB; s <= Card.SPADE; s++)
            for (int r = Card.ACE; r <= Card.KING; r++) {
                deckCard.add(new Card(s, r))
            }

        for (int i = 1; i <= genCount; i++) {
            shuffle(deckCard)
            int indDeck = 0
            Card[] fc = new Card[5]
            int ipos = 0
            while (indDeck < deckCard.size()) {
                fc[ipos] = deckCard[indDeck]
                indDeck++
                ipos++
                if (ipos == 5) {
                    p5CardsList.add(new FiveCards(fc))
                    ipos = 0
                }
            }
        }

        // Add More Sample Data
        Card[] fourCards = [new Card(CLUB, 1), new Card(DIAMOND, 1), new Card(HEART, 1), new Card(SPADE, 1), new Card(CLUB, 2)]
        p5CardsList.add(new FiveCards(fourCards))

        Card[] fullHouse = [new Card(CLUB, 1), new Card(DIAMOND, 1), new Card(HEART, 1), new Card(SPADE, 13), new Card(CLUB, 13)]
        p5CardsList.add(new FiveCards(fullHouse))

        Card[] straight = [new Card(CLUB, 1), new Card(DIAMOND, 2), new Card(HEART, 3), new Card(SPADE, 4), new Card(CLUB, 5)]
        p5CardsList.add(new FiveCards(straight))

        Card[] flush = [new Card(CLUB, 1), new Card(CLUB, 2), new Card(CLUB, 3), new Card(CLUB, 4), new Card(CLUB, 6)]
        p5CardsList.add(new FiveCards(flush))

        Card[] straightFlu = [new Card(CLUB, 1), new Card(CLUB, 2), new Card(CLUB, 3), new Card(CLUB, 4), new Card(CLUB, 5)]
        p5CardsList.add(new FiveCards(straightFlu))

        Card[] twoPair = [new Card(CLUB, 1), new Card(DIAMOND, 1), new Card(HEART, 10), new Card(SPADE, 10), new Card(CLUB, 2)]
        p5CardsList.add(new FiveCards(twoPair))

        Card[] onePair = [new Card(CLUB, 1), new Card(DIAMOND, 1), new Card(HEART, 4), new Card(SPADE, 5), new Card(CLUB, 6)]
        p5CardsList.add(new FiveCards(onePair))

        Card[] noPair = [new Card(CLUB, 1), new Card(DIAMOND, 3), new Card(HEART, 5), new Card(SPADE, 7), new Card(CLUB, 9)]
        p5CardsList.add(new FiveCards(noPair))

        return p5CardsList
    }

    static void shuffle(List<Card> list) {
        final int count = 100
        Random rand = new Random(1234)
        int oneZero
        int lSize = list.size()
        int ind = 0
        for (int i = 1; i <= count * lSize; i++) {
            oneZero = rand.nextInt(2)
            if (oneZero == 0) list.add(list.remove(ind))
            else {
                ind++
                ind %= lSize
            }
        }
    }

    static void printConvertedList(List<Entry> fcList) {
        // Entry.fiveCards = Original FiveCards Data
        // Entry.transform = Converted Poker Data
        int cCount = 0
        for (Entry fc : fcList) {
            String print = "${++cCount}\t ${fc.fiveCards.toString()} \t -> "
            switch (fc.transform[0]) {
                case 1: print += "No Pair"; break
                case 2: print += "One Pair"; break
                case 3: print += "Two Pair"; break
                case 4: print += "Triple Pair"; break
                case 5: print += "Full House"; break
                case 6: print += "Four Cards"; break
            }
            print += " : ${fc.transform.toString()}"
            println(print)
        }
    }

    static main(args) {
        List<FiveCards> list5card = generate5CardList(10)

        println "FiveCards Original Data"
        list5card.eachWithIndex { item, index ->
            println("${index + 1}\t ${item}")
        }

        List<Entry> pokerLowOrder = Modules.setPokerLowOrder(list5card)

        println "\n"
        println "Poker Low Order"
        Closure comp = { Entry left, Entry right ->
            // This comparator is Poker Low Order
            Integer size
            if (left.transform.size() > right.transform.size()) size = right.transform.size()
            else size = left.transform.size()
            // List size is different, so SIZE VARIABLE is based on the small size
            for (Integer i = 0; i < size; i++) {
                def temp = left.transform[i] <=> right.transform[i]
                if (temp != 0) return temp
            }
            // Entry.fiveCards = Original FiveCards Data
            // Entry.transform = Converted Poker Data
            return 0
        }
        List<Entry> list5cardSorted = new QuickSort().sort(pokerLowOrder, comp)
        printConvertedList(list5cardSorted)
    }
}
