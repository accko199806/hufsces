package hufs.ces.clas.polymorphism

import hufs.ces.clas.Entry
import hufs.ces.clas.IPhoneBook

class PhoneBookList implements IPhoneBook {

    private List<Entry> phoneBookList;

    PhoneBookList() {
        phoneBookList = [];
    }

    int findLoc(String name) {
        for (int i = 0; i < phoneBookList.size(); ++i) {
            if (phoneBookList[i].phoneName == name)
            // phoneBookList[i].phoneName.equals(name) in Java
                return i;
        }
        return -1; // not found
    }

    @Override
    int find(String name) {
        int loc = findLoc(name);
        if (loc == -1)
            return -1; // not found
        return phoneBookList[loc].phoneNumber;
    }

    @Override
    String find(int number) {
        for (int i = 0; i < phoneBookList.size(); ++i) {
            if (phoneBookList[i].phoneNumber == number)
                return phoneBookList[i].phoneName;
        }
        return "not found"; // not found
    }

    @Override
    boolean insert(String name, int number) {
        int loc = findLoc(name);
        if (loc == -1) { //  can insert
            phoneBookList.add(new Entry(name, number));
            return true;
        } else {
            return false;
        }
    }

    @Override
    boolean update(String name, int number) {
        def loc = findLoc(name);
        if (loc != -1) { // location을 불러와서 번호를 변경시킴.
            phoneBookList[loc].phoneNumber = number;
            return true;
        } else {
            println "***Error -- Name not found";
            return false;
        }
    }

    @Override
    boolean remove(String name) {
        int loc = findLoc(name);
        if (loc != -1) { // there exist name
            // remove array entry at loc
            phoneBookList.remove(loc);
            return true;
        } else {
            return false;
        }
    }

    @Override
    void listAll() {
        println "Name\tNumber";
        for (int i = 0; i < phoneBookList.size(); ++i) {
            println "${phoneBookList[i].phoneName}\t${phoneBookList[i].phoneNumber}"
        }
    }
}
