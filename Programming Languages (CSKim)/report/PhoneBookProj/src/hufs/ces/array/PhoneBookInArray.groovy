package hufs.ces.array

MAX_ENTRY = 10;

nameData = ["Park SH", "Kang JH", "Kim KS", "Lee YH", "Kang SH"];
numberData = [5023, 5002, 5008, 5067, 5038];

arrayPhoneBook = new Entry[MAX_ENTRY];
lastp = 0;

def findLoc(def name){
	for (def i=0; i<lastp; ++i){
		if (arrayPhoneBook[i].phoneName == name)
			return i;
	}
	return -1; // not found
}

def find(String name){
	for (def i=0; i<lastp; ++i){
		if (arrayPhoneBook[i].phoneName == name)
			return arrayPhoneBook[i];
	}
	return new Entry("not found", -1); // not found
}

def find(int number){
	for (def i=0; i<lastp; ++i){
		if (arrayPhoneBook[i].phoneNumber == number)
			return arrayPhoneBook[i];
	}
	return new Entry("not found", -1); // not found
}

def insert(def name, def number){
	def loc = findLoc(name);
	if (loc == -1){
		// insert
		if (lastp >= MAX_ENTRY){
			println "***Error -- PhoneBook Overflow";
		}
		else {
			arrayPhoneBook[lastp] = new Entry(name, number);
			lastp++;
		}
	} else {
		println "***Error -- Duplicated Name [${name}]";
	}
}

def remove(def name){
	def loc = findLoc(name);
	if (loc != -1) { // there exist name
		// remove array entry at loc
		for (def i=loc+1; i<lastp; ++i)
			arrayPhoneBook[i-1] = arrayPhoneBook[i]
		lastp--;
	} else {
		println "***Error -- Name not found";
	}
}

def update(def name, def num) {
	def entry = find(name);
	if (entry != null) {
		entry.phoneNumber = num
	} else {
		println "***Error -- Name not found";
	}
}

def listAll(){
	println "Name\tNumber";
	for (def i=0; i<lastp; ++i)
		println "${i}\t${arrayPhoneBook[i].phoneName}\t" +
				"${arrayPhoneBook[i].phoneNumber}"
}

/** MAIN AREA **/

println "리스트 첫 번째 업데이트";

incount = nameData.size();
for (def i=0; i < incount; ++i){
	insert(nameData[i], numberData[i]);
}

println "리스트 업데이트 완료\n";
listAll();
println "\n자신만의 고유 이름 추가 3명";

insert("Gwon PG", 8989);
insert("Lee SG", 6666);
insert("Kim NR", 7777);

listAll();

println "\nGwon PG의 번호를 8989에서 5555로 변경";
update("Gwon PG", 5555);

listAll();

println "\nKim NR, Lee SG의 번호를 삭제";
remove("Kim NR");
remove("Lee SG");

listAll();

println "\n이름으로 번호 찾기 (Gwon PG) - ${find("Gwon PG").phoneNumber}";
println "번호로 이름 찾기 (5555) - ${find(5555).phoneName}\n";

println "[테스트케이스] insert - duplicate"
insert("Gwon PG", 8989);

println "\n[테스트케이스] find - not found"
println "이름 Kim NR - ${find("Kim NR").phoneNumber}";
println "번호 1234 - ${find(1234).phoneName}\n";

println "리스트 업데이트 완료\n";
listAll();