class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price;
        self.speed = speed;
        self.fuel = fuel;
        self.mileage = mileage;

    def tax(self):
        if (self.price > 10000):
            self.tax = 0.15;
        else:
            self.tax = 0.12;
        return self;

    def display_all(self):
        print("Price:", self.price)
        print("Speed:", self.speed)
        print("Fuel:", self.fuel);
        print("Mileage:", self.mileage);
        print("Tax:", self.tax);
        return self;

car1 = Car(2000, "20mph", "half", "10mpg")
car2 = Car(200, "80mph", "full", "42mpg")
car3 = Car(20000, "65mph", "1/8th", "30mpg")
car4 = Car(1000, "60mph", "half", "20mpg")
car5 = Car(1200, "40mph", "empty", "15mpg")
car6 = Car(200000, "5mph", "half", "11mpg")


car1.tax().display_all();
print()
car2.tax().display_all();
print()
car3.tax().display_all();
print()
car4.tax().display_all();
print()
car5.tax().display_all();
print()
car6.tax().display_all();