###
#ANIMAL CLASS
###
class Animal(object):
    def __init__(self, name, health):
        self.name = name;
        self.health = health;

    def walk(self):
        self.health -= 1;
        return self;
    
    def run(self):
        self.health -= 5;
        return self;
    
    def displayHealth(self):
        print(self.health);
        return self;

ditto = Animal("Dittopix", 100);

ditto.walk().walk().walk().run().run().displayHealth();

###
#DOG CLASS
###

class Dog(Animal):
    def __init__(self, name):
        self.name = name;   
        self.health = 150;           
    def pet(self):
        self.health += 5;
        return self;

growlithe = Dog("Admiral");

growlithe.walk().walk().walk().run().run().pet().displayHealth();

###
#Dragon Class
###

class Dragon(Animal):
    def __init__(self, name):
        self.name = name;
        self.health = 170;
    def fly(self):
        self.health -= 10;
        return self;
    def displayHealth(self):
        super(Dragon, self).displayHealth();
        print("It's a fucking dragon!")


#Now try creating a new Animal and confirm that it can not call the pet() and fly() methods, 
#and its displayHealth() is not saying 'this is a dragon!'. Also confirm that your Dog class can not fly()

dratini = Dragon("Drat");

dratini.fly().fly().displayHealth();

growlithe.fly().displayHealth();