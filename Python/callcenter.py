##Assignment: Call Center

class Call(object):
    def __init__(self, id, name, phone, time, reason):
        self.id = id;
        self.name = name;
        self.phone = phone;
        self.time = time;
        self.reason = reason;

    def displayInfo(self):
        print("ID:", self.id)
        print("Caller:", self.name)
        print("Callback:", self.phone)
        print("Call Time:", self.time)
        print("Reason:", self.reason)


tempCall = Call(1175, "Joanie Smott", "3017-653-9981", "04:15:57pst", "Cancelling Wedding");
#empCall.displayInfo();

class CallCenter(object):
    def __init__(self):
        self.calls = [];
        self.queue = 0;

    def addCall(self, call):
        self.calls.append(call);
        self.queue += 1;
        return self;
    
    def removeCall(self):
        self.calls.remove(self.calls[0]);
        self.queue -= 1;
        return self
    
    def debug(self):
        print(self.calls)

    def infoList(self):
        for i in range(0, len(self.calls)):
            print("FFS", self.calls[i].name)
            print("OMFG", self.calls[i].phone)
            print(self.queue)

thecall = Call(12345, "JJ Wiley", "206-637-2240", "00:00:01", "to whine")
missedcall = Call(567899, "Alexandra", "206-456-7891", "02:06:07", "Fix program")
mahCenter = CallCenter(); 
mahCenter.addCall(missedcall)
mahCenter.addCall(tempCall);
mahCenter.addCall(thecall).infoList();
mahCenter.removeCall().infoList();


#mahCenter.addCall(1175, "Joanie Smott", "3017-653-9981", "04:15:57pst", "Cancelling Wedding");
#mahCenter.calls.displayInfo();