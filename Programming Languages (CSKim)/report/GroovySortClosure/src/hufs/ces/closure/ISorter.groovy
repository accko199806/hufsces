package hufs.ces.closure

interface ISorter<T> {
	
	List<T> sort(List<T> list);
	List<T> sort(List<T> list, Closure comp);
	
}
