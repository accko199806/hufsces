package hufs.ces.closure

class QuickSort<T> implements ISorter<T>{

    List<T> sort(List<T> list, Closure comp) {
        list = list.collect()
        quickSort(list, comp)
        return list
    }

    static <T> void quickSort(List<T> list, Closure<T> comp) {
        int n = list.size()
        if (n < 2) return

        List<T> list1 = []
        List<T> list2 = []
        List<T> listEq = []

        T pivot = list[0]

        while (!list.isEmpty()) {
            if (comp(list[0], pivot) < 0) {
                list1.add(list[0])
            } else if (comp(list[0], pivot) == 0) {
                listEq.add(list[0])
            } else {
                list2.add(list[0])
            }
            list.remove(0)
        }
        quickSort(list1, comp)
        quickSort(list2, comp)

        list.addAll(list1)
        list.addAll(listEq)
        list.addAll(list2)
    }
}
