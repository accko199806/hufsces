package hufs.ces.poker

import java.util.ArrayList
import java.util.List

class SelSort<T> implements ISorter<T> {

	@Override
	public List<T> sort(List<T> list) {
		return selSort(list);

	}
	@Override
	public List<T> sort(List<T> list, Comparator<T> comp) {
		return selSort(list, comp);
	}

	static<T> void swapNode(List<T> list, int p, int q) {
		T tempNode = list[p];
		list[p] = list[q];
		list[q] = tempNode;
	}
	static<T> int getMinIndex(List<T> list, int rest) {
		assert rest >= 0 && rest < list.size();
		int minInd = rest;
		for (int i=rest+1; i<list.size(); ++i) {
			if (list[i] < list[minInd]) {
				minInd = i;
			}
		}
		return minInd;
	}
	static<T> int getMinIndex(List<T> list, int rest, Comparator<T> comp) {
		assert rest >= 0 && rest < list.size();
		int minInd = rest;
		for (int i=rest+1; i<list.size(); ++i) {
			if (comp.compare(list[i], list[minInd]) < 0 ) {
				minInd = i;
			}
		}
		return minInd;
	}
	static<T> List<T> selSort(List<T> list) {
		list = list.collect();
		int lsize = list.size();
		for (int i=0; i<lsize; ++i){
			int minit = getMinIndex(list, i);
			swapNode(list, i, minit);
		}
		return list;
	}
	static<T> List<T> selSort(List list, Comparator<T> comp) {
		list = list.collect();
		int lsize = list.size();
		for (int i=0; i<lsize; ++i){
			int minit = getMinIndex(list, i, comp);
			swapNode(list, i, minit);
		}
		return list;
	}
	static void printList(List list) {
		final int  LINE_MAX = 13;
		int i = 0;
		for (def c:list) {
			print "$c ";
			i++;
			if (i % LINE_MAX == 0) println();
		}
		println();
	}

	static main(args) {

		List<Card> deck = [];
		// Make a Card Deck
		for (int s=Card.CLUB; s<=Card.SPADE; s++) {
			for (int r=Card.ACE; r<=Card.KING; r++){
				deck.add(new Card(s,r));
			}
		}
		
		ISorter sorter = new SelSort();
		println "List before ${sorter.class.getName()}";
		printList(deck);
		println "List after ${sorter.class.getName()}"
		printList(sorter.sort(deck));

		println "List before ${sorter.class.getName()}";
		printList(deck);
		println "List after ${sorter.class.getName()} with String comp"
		printList(sorter.sort(deck, new StringCardComparator()));
		
		def l1 = [3, 2, 7, 6, 8, 4, 5];
		printList(l1);
		printList(sorter.sort(l1));

	}

}
