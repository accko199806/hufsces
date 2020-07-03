package hufs.ces.poker

class MyFiveCardsComparator implements Comparator<FiveCards> {

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
}