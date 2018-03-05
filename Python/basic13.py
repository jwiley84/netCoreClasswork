#FIRST (one)
for count in range(0,256):
    print(count)

#SECOND

for count in range(1,256):
    if (count % 2 != 0):
        print(count)


#THIRD

sum = 0;
for count in range(0,256):
    print(count);
    sum += count;
    print(sum);



#FOURTH
setArr = [1,2,3,4,5];

for count in setArr:
    print(count);



#FIFTH

setArr = [1,2,3,4,5];

print(max(setArr));


#SIXTH
setArr = [1,2,3,4,5];
total = 0;

for count in setArr:
    total += count;
total = total/len(setArr)

print(total)

#SEVENTH
newArr = [];

for count in range(1,256):
    if (count % 2 != 0):
        newArr.append(count)

print(newArr)


#EIGHT:
setArr = [1,2,3,4,5];

for count in range(0,len(setArr)):
    setArr[count] = setArr[count] * setArr[count]

print(setArr)


#NINE:
setArr = [1,2,3,4,5];
y = 3;
amt = 0;

for count in setArr:
    if (count > y):
        print(count)
        amt += 1;


print("amount is: " + str(amt))



#TEN:
setArr = [1,-2,3,-4,5];

for count in range(0,len(setArr)):
    if (setArr[count] < 0):
        setArr[count] = 0;
print(setArr)



#ELEVEN:
setArr = [1,2,3,4,5];
sum = 0;

print(max(setArr))
print(min(setArr))

for count in setArr:
    sum += count;
sum = sum/(len(setArr))

print(sum)




#TWELVE:
setArr = [1,2,3,4,5];
#output = [2, 3, 4, 5, 0]

for count in range(0,len(setArr)-1):
    setArr[count] = setArr[count + 1]



setArr[len(setArr)-1] = 0;
print(setArr);


#THIRTEEN
setArr = [-1,2,-3,4,-5];

for count in range(0,len(setArr)):
    if (setArr[count] < 0):
        setArr[count] = "Dojo";
print(setArr)