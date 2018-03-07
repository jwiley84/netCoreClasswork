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
