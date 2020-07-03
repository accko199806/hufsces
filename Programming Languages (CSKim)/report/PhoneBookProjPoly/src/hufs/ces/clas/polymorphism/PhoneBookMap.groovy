package hufs.ces.clas.polymorphism

import hufs.ces.clas.IPhoneBook

class PhoneBookMap implements IPhoneBook {

    private Map<String, Integer> phoneBookMap;

    PhoneBookMap() {
        phoneBookMap = [:];
    }

    @Override
    int find(String name) {
        Integer pnumber = phoneBookMap[name];
        if (pnumber != null) {
            return pnumber;
        } else {
            return -1;
        }
    }

    @Override
    String find(int number) {
        String temp = "not found"
        for (Map.Entry<Integer, String> entry : phoneBookMap.entrySet()) {
            if (entry.getValue() == number) temp = entry.getKey();
        }
        return temp;
    }

    @Override
    boolean insert(String name, int number) {
        if (find(name) == -1) { // insert
            //phoneBookMap.put(name, number); // Java style
            phoneBookMap[name] = number; // Groovy style
            return true;
        } else {
            return false;
        }
    }

    @Override
    boolean update(String name, int number) {
        if (find(name) != -1) { // update
            //phoneBookMap.put(name, number); // Java style
            phoneBookMap[name] = number; // Groovy style
            return true;
        } else {
            return false;
        }
    }

    @Override
    boolean remove(String name) {
        if (find(name) != -1) { // remove
            phoneBookMap.remove(name);
            return true;
        } else {
            return false;
        }
    }

    @Override
    void listAll() {
        println "Name\tNumber";
        phoneBookMap.each { pname, pnumber -> println "${pname}\t${pnumber}" }
    }
}
