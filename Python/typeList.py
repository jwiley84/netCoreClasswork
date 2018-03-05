#this is literally what I just did....abs

#input
l1 = ['magical unicorns',19,'hello',98.98,'world']
l2 = [2,3,1,7,4,12]
l3 = ['magical','unicorns']
strCount = 0;
intCount = 0;
newStr = '';
newTotal = 0;


#test
for item in l1:
    if (type(item) is int):
        intCount += 1;
        newTotal += item;
    elif(type(item) is float):
        intCount += 1;
        newTotal += item;
    elif (type (item) is str):
        strCount +=1;
        newStr += item;
    
if (strCount > 0 and intCount > 0):
    print("this is a mixed list")
    print(newStr)
    print(newTotal)
elif (intCount == 0):
    print("this is a string list")
    print(newStr)
else:
    print("This is an integer list")
    print(newTotal)


#instructions
'''
Write a program that takes a list and prints a message
 for each element in the list, based on that element's
      data type.

Your program input will always be a list. For each item
 in the list, test its data type. If the item is a string, 
 concatenate it onto a new string. If it is a number, add 
 it to a running sum. At the end of your program print the 
 string, the number and an analysis of what the list contains.
  If it contains only one type, print that type, otherwise,
   print 'mixed'.

Here are a couple of test cases. Think of some of your own, 
too. What kind of unexpected input could you get?
'''