import random;

class Patient(object):
    def __init__(self, name, caseNo, allergies, majorInjury):
        self.name = name;
        self.caseNo = caseNo;
        self.allergies = allergies;
        self.majorInjury = majorInjury;
        self.bedNo = "none";

    def displayInfo(self):
        print("Name:", self.name)
        print("Case Number:", self.caseNo)
        print("Allergies:", self.allergies)
        print("Major Injury:", self.majorInjury)

LolaHayes = Patient("Lola Hayes", 123456, "Cheese", "Fell off stage rigging");
DianaStanly = Patient("Diana Stanley", 2468135, "wool, wheat", "Stabbed in arm");
MarkHarrigan = Patient("Mark Harrigan", 153975, "sunlight", "shot in foot")
RolandBanks = Patient("Roland Banks", 987654, "the color green", "Tripped on Curb")
#LolaHays.displayInfo();

class Hospital(object):
    def __init__(self, name):
        self.patientList = [];
        self.capacity = 100;
        self.name = name;

    def admitPatient(self, patient):
        self.patientList.append(patient);
        self.capacity -= 1;
        patient.bedNo = random.randint(1,100);

    def dischargePatient(self, patientName):
        for i in self.patientList:
            if (patientName == self.patientList[i].name):
                self.patientList.remove(self.patientList[i]);
                self.patientList[i].bedNo = "none";

StMarys = Hospital("StMarys");

StMarys.admitPatient(MarkHarrigan);
print(StMarys.patientList[0].name)
