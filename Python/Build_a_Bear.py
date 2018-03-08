class User(object):
    #init method is called every time a new object is created
    def __init__(self, name, email):
        #set some instance variables.
        self.name = name;
        self.email = email;
        self.logged = False;

    #login is a method used to help a user login. no shit?
    def login(self, id):
        self.logged = True;
        print(self.name + " is logged in");
        return self; #this returns the the instance that called it (such 
        #as 'jessica' or 'jennifer')
    



#class className(inherit--typically 'object'):
    #code goes here
 
#class declaration is a blueprint. Once we've finished, we can create instances
#using this blueprint.
new_user = User("Jessica", "jess.m.wailes@gmail.com")
print(new_user.email)
print(new_user.name)
print(new_user.logged)


#jessica = User() #creates instance of 'user' as Jessica
#jennifer = User()
#print(jessica, jennifer)


class Vehicle(object):
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0
    def drive(self,miles):
        self.mileage += miles
        return self
    def reverse(self,miles):
        self.mileage -= miles
        return self
class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"
class Car(Vehicle):
    def set_wheels(self):
        self.wheels = 4
        return self
class Airplane(Vehicle):
    def fly(self, miles):
        self.mileage += miles
        return self
v = Vehicle(4,8,"dodge","minivan")
print v.make
b = Bike(2,1,"Schwinn","Paramount")
print b.vehicle_type()
c = Car(8,5,"Toyota", "Matrix")
c.set_wheels()
print c.wheels
a = Airplane(22,853,"Airbus","A380")
a.fly(580)
print a.mileage

#SPLAT
'''
Multiple Arguments
What if you want to pass in a variable number of arguments, or want to capture multiple arguments into a single parameter? Placing an asterisk before the name of the parameter after the "normal'' parameters does just that. The asterisk is called a 'splat' operator.

def varargs(arg1, *args):
  print "Got "+arg1+" and "+ ", ".join(args)
varargs("one") # output: "Got one and "
varargs("one", "two") # output: "Got one and two"
varargs("one", "two", "three") # output: "Got one and two, three"
In this example, the first argument is assigned to the first method parameter as 
sual. However, the next parameter is prefixed with an asterisk(the "splat" operator 
we just introduced), which bundles the remaining arguments into a new tuple, which 
is then assigned to that parameter.

If we tested the type of args inside our function using type(args) we would get:

def varargs(arg1, *args):
   print "args is of " + str(type(args))
 varargs("one", "two", "three") # output: args is of <type 'tuple'>
Note the .join() method is called on a string that glues the values in the tuple 
together. For example, the tuple of arguments ('two', 'three') was joined as 'two, 
three' when we called ', '.join(args) .


Super
Sometimes in your OOP code, you will want to create updated versions of methods that are defined in the parent class, because in addition to your custom code you want specifically to call the parent implementation of that method as well (or instead). In these cases, you would reference that parent object with the keyword ' super'. Specifically you reference that parent's method by calling 'super(ChildClassName, self).parent_method()'.  

Parent __init__
One thing we may want to do is call the Parent class's __init__ method, but also have our Child class change attributes defined by its Parent class. Say that we wanted each of our sub-classes (Wizard, Ninja, Samurai) to still inherit the attributes of the parent Human class but have more developed attributes than the average Human.  We could do that like this:

from human import Human
class Wizard(Human):
    def __init__(self):
        super(Wizard, self).__init__()   # use super to call the Human __init__ method
        self.intelligence = 10           # every wizard starts off with 10 intelligence
    def heal(self):
        self.health += 10
class Ninja(Human):
    def __init__(self):
        super(Ninja, self).__init__()    # use super to call the Human __init__ method
        self.stealth = 10                # every Ninja starts off with 10 stealth
    def steal(self):
        self.stealth += 5
class Samurai(Human):
    def __init__(self):
        super(Samurai, self).__init__()  # use super to call the Human __init__ method
        self.strength = 10               # every Samurai starts off with 10 strength
    def sacrifice(self):
        self.health -= 5
If we create instances of each, we'll see that they have the same attributes as the typical 
Human (the parent class), but they also have beefed up attributes depending on which subclass 
we instantiated! Notice how we call the __init__ method of the super(parent). Other methods 

are called the same way with the exception of passing in variables. We left that exercise for you !
'''