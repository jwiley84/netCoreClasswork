#comment
'''
Assignment: String and List Practice
Use only the built-in methods and functions from the previous tabs to do the following exercises. You will find the following methods and functions useful:

• .find()
• .replace()
• min()
• max()
• .sort()
• len()


New List
Start with a list like this one:
 x = [19,2,54,-2,7,12,98,32,10,-3,6]. 
 Sort your list first. Then, split your list in half. 
 Push the list created from the first half to position 
 0 of the list created from the second half. The output 
 should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. 
 Stick with it, this one is tough!
'''

words = "It's Thanksgiving day! It's my birthday, too!"
words.find("day")
work = words.replace("day", "month")
print(work)

x = [2,54,-2,7,12,98]
print(min(x))
print(max(x))

x = ["hello",2,54,-2,7,12,98,"world"]
print(x[0]);
print(x[len(x)-1])
y = []
y.append(x[0])
y.append(x[len(x)-1])
print(y)

zx = [19,2,54,-2,7,12,98,32,10,-3,6]
zx.sort()
print(zx)
#print(len(zx))
#mep = (zx[0:5])
blep = []

for item in range(0,5):
    blep.append(zx[item])
   
print(blep)
for item in range(0,5):
    zx.pop()

print(zx)

zx.append(zx)
for item in zx:
    temp = zx[len(zx)-1]
    zx[item]
