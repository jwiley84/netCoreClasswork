class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price;
        self.max_speed = max_speed;
        self.miles = miles;

    def displayinfo(self):
        print("Price:", self.price);
        print("Max Speed:", self.max_speed);
        print("Miles:", self.miles);

        return self;
    
    def ride(self):
        #self.riding = True;
        print("Riding")
        self.miles += 10;

        return self;

    def reverse(self):
        print("Reversing...")
        self.miles -= 5;
        return self;


bike1 = Bike(200, "5mph", 1000)
bike2 = Bike(100, "3mph", 4000)
bike3 = Bike(1000, "25mph", 100)

print("bike 1")
bike1.ride().ride().ride().reverse().displayinfo()

print("bike 2")
bike2.ride().ride().reverse().reverse().displayinfo()

print("bike 3")
bike3.reverse().reverse().reverse().displayinfo();
    