package hufs.ces.closure

import java.util.ArrayList
import java.util.List

class QuickSort<T> implements ISorter<T> {
	
	@Override
	public List<T> sort(List<T> list) {
		list = list.collect();
		quickSort(list);
		return list;
	}
	@Override
	public List<T> sort(List<T> list, Closure<T> comp) {
		list = list.collect()
		quickSort(list, comp);
		return list;
	}
	static<T> void quickSort(List<T> list) {
		int n = list.size();
		if (n < 2)
			return;

		List<T> list1 = [];
		List<T> list2 = [];
		List<T> listEq = [];

		T pivot = list[0];

		while (!list.isEmpty()) {
			if (list[0] < pivot) {
				list1.add(list[0]);
			}
			else if (list[0] == pivot) {
				listEq.add(list[0]);
			}
			else {
				list2.add(list[0]);
			}
			list.remove(0);
		}
		quickSort(list1);
		quickSort(list2);

		list.addAll(list1);
		list.addAll(listEq);
		list.addAll(list2);
	}
	static<T> void quickSort(List list, Closure<T> comp) {
		int n = list.size();
		if (n < 2)
			return;

		List<T> list1 = [];
		List<T> list2 = [];
		List<T> listEq = [];

		T pivot = list[0];

		while (!list.isEmpty()) {
			//println "${list[0]},${list[0].getClass()} -- ${pivot}, ${pivot.getClass()} "
			if (comp(list[0],pivot) < 0) {
				list1.add(list[0]);
			}
			else if (comp(list[0],pivot) == 0) {
				listEq.add(list[0]);
			}
			else {
				list2.add(list[0]);
			}
			list.remove(0);
		}
		quickSort(list1, comp);
		quickSort(list2, comp);

		list.addAll(list1);
		list.addAll(listEq);
		list.addAll(list2);
	}

}
