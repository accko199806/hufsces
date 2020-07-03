package hufs.ces.closure

class SelSort<T> implements ISorter<T> {

    @Override
    List<T> sort(List<T> list, Closure comp) {
        return selSort(list, comp)
    }

    static <T> void swapNode(List<T> list, int p, int q) {
        T tempNode = list[p]
        list[p] = list[q]
        list[q] = tempNode
    }

    static <T> int getMinIndex(List<T> list, int rest, Closure comp) {
        assert rest >= 0 && rest < list.size()
        int minInd = rest
        for (int i = rest + 1; i < list.size(); ++i) {
            if (comp(list[i], list[minInd]) < 0) {
                minInd = i
            }
        }
        return minInd
    }

    static <T> List<T> selSort(List<T> list, Closure comp) {
        list = list.collect()
        int lsize = list.size()
        for (int i = 0; i < lsize; ++i) {
            int minit = getMinIndex(list, i, comp)
            swapNode(list, i, minit)
        }
        return list
    }
}
