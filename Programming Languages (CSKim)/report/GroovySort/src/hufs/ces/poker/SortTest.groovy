package hufs.ces.poker

class SortTest {

	static void printList(List list) {
		final int  LINE_MAX = 13;
		int i = 0;
		for (Card c:list) {
			print "$c ";
			i++;
			if (i % LINE_MAX == 0) println();
		}
		println();
	}
	static void sortTest(ISorter sorter) {

		List<Card> deck = [];
		// Make a Card Deck
		for (int s=Card.CLUB; s<=Card.SPADE; s++) {
			for (int r=Card.ACE; r<=Card.KING; r++){
				deck.add(new Card(s,r));
			}
		}

		println "List before ${sorter.class.getName()}";
		printList(deck);
		println "List after ${sorter.class.getName()}"
		printList(sorter.sort(deck));

		println "List before ${sorter.class.getName()}";
		printList(deck);
		println "List after ${sorter.class.getName()} with String comp"
		printList(sorter.sort(deck, new StringCardComparator()));
	}
	static main(args) {

		sortTest(new SelSort());

		sortTest(new QuickSort());
	}

}
