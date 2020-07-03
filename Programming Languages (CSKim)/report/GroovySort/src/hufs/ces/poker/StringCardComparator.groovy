package hufs.ces.poker

class StringCardComparator implements Comparator<Card> {
	public int compare(Card left, Card right) {
		if (left.toString().compareTo(right.toString()) < 0)
			return -1;
		else if (left.toString().compareTo(right.toString()) > 0)
			return 1;
		else
			return 0;
	}
}
