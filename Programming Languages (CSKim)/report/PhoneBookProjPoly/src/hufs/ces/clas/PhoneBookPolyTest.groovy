package hufs.ces.clas

import hufs.ces.clas.polymorphism.PhoneBookArray
import hufs.ces.clas.polymorphism.PhoneBookList
import hufs.ces.clas.polymorphism.PhoneBookMap

class PhoneBookPolyTest {

    static void testPhoneBook(IPhoneBook pbook) {

        println "*** Test ${pbook.class} PhoneBook ***";

        String[] nameData = ["Park SH", "Kang JH", "Kim KS", "Lee YH", "Kang SH"];
        int[] numberData = [5023, 5002, 5008, 5067, 5038,];

        for (int i = 0; i < nameData.length; ++i) {
            pbook.insert(nameData[i], numberData[i]);
        }

        println "List All Inserted Entry";
        pbook.listAll();

        println "\nInsert 3 Name";
        if (!pbook.insert("Gwon PG", 8989)) { // 1
            println "***Error in Insert -- Gwon PG ***";
        }
        if (!pbook.insert("Lee SG", 6666)) { // 2
            println "***Error in Insert -- Lee SG ***";
        }
        if (!pbook.insert("Kim NR", 7777)) { // 3
            println "***Error in Insert -- Kim NR ***";
        }
        pbook.listAll();

        println "\nChange The Number of Gwon PG - 8989 to 5555";
        if (!pbook.update("Gwon PG", 5555)) {
            println "***Error in Update -- Kang JH ***";
        };
        pbook.listAll();

        println "\nDelete Entry - Kim NR, Lee SG";
        if (!pbook.remove("Kim NR")) {
            println "***Error in Remove -- Kim NR ***";
        };
        if (!pbook.remove("Lee SG")) {
            println "***Error in Remove -- Lee SG ***";
        };
        pbook.listAll();

        println("\n[TestCase] Find Number")
        println "Find Number By Name (Gwon PG) - ${pbook.find("Gwon PG")}";
        println "Find Number By Number (5555) - ${pbook.find(5555)}\n";

        println "[TestCase] insert - duplicate"
        if (!pbook.insert("Gwon PG", 8989)) { // duplicate
            println "***Error in Insert -- Gwon PG ***";
        }

        println "\n[TestCase] find - not found"
        if (pbook.find("Kim NR") != -1) println "Name Kim NR - ${pbook.find("Kim NR")}";
        else println "Name Kim NR - NOT FOUND";
        if (pbook.find(1234) != "not found") println "Number 1234 - ${pbook.find(1234)}\n";
        else println "Number 1234 - NOT FOUND";

        println "\n***List All Updated Entry";
        pbook.listAll();
        println("\n");
    }

    static main(args) {
        testPhoneBook(new PhoneBookArray());
        testPhoneBook(new PhoneBookList());
        testPhoneBook(new PhoneBookMap());
    }
}