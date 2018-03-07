import math

#try again
'''
def frustrated():
    for item in range(0,100):
        if (item < 2):
            print(item)
        else:
            if (((item**0.5)**2) == item):
                print(str(item) + " woot!")
            else:
                print(item)

#frustrated();

#for item in range(0,100000):
#    if (item < 2):
#        continue;
#    elif (math.sqrt(item) )

'''

def frustratedRoundTwo(num):
    item = 1
    while (item < num+1):
        #testin for prime
        if (num % 2 != 0):
            if (num % item != 0):
                print("FOO")

        #test for perfect sqares
        sqrt = (item**.5) % 1
        if (item == 1):
            print("BAR! (neither 1 nor 0s are techically prime")
        elif (item == 2):
            print("FOO BAR (I am the smallest and only even prime!")
        elif (sqrt == 0):
            print("BAR!")
        elif (sqrt != 0 and num % item == 0): 
            print(item)
        print(item)
        item +=1



frustratedRoundTwo(10)
#hash me
'''
num = 11
for index in range(2, num):
    print("index {} mod {}".format(index, (num % index)))
    #print(num % index)
    if (num % index == 0):
        print("false")
        break;
    else: 
        print("FOO")

#for item in range(3,6):
#    text = item/2;
#    print(item, text);

for item in range(0,5):
    sqrt = (item**.5) % 1
    print(sqrt)
'''