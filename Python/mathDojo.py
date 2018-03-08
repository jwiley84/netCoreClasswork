###
#INSTRUCTIONS
###
'''
HINT: To do this exercise, you will probably have to use 'return self'. If the method returns itself (an instance of itself), we can chain methods.

PART I
Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.

Then create a new instance called md. It should be able to do the following task:

md.add(2).add(2,5).subtract(3,2).result
which should perform 0+2+(2+5)-(3+2) and return 4.

PART II
Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter with 
any number of values passed into the list. It should now be able to perform the 
following tasks:

md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result.

PART III
Make any needed changes in MathDojo in order to support tuples of values in addition to lists and singletons.
'''

class MathDojo(object):
    def __init__(self):
        self.total = 0;

    def add(self, *x):
        exs = [];
        for num in x:
            if (type(x) is int):
                exs.append(num);
            else:
                for num in num[x]:
                    exs.append(x)

        print(exs);
        #for num in ex:
        #    print("num", num)
        #    self.total += num
        #    print("add total", self.total)
        #print(ex)
        #self.total += y;
        return self;

    def subtract(self, *x):
        exs = [];
       
        for num in x:
            if (type(x) is list):
                exs.append(num[x]);
            else:
                exs.append(num)

        print(exs);
            #for num in exs:
                #self.total -= num;
            #print("sub. total", self.total)
        #self.total -= y;
        return self;

    def result(self):
        print("total", self.total);
        #return result;

md = MathDojo();
print("One")
#md.add(2).add(2, 5).subtract(3,2).result();
#which should perform 0+2+(2+5)-(3+2) and return 4.
#print("two")
md.add([1], 3,4).result()
#should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result.