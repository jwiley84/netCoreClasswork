#PRINT ALL MULTIPLES OF 2 FROM 0 TO 1000. 

for number in range(0,1001):
    if (number % 2 == 0): 
        print(number)


#PRINT ALL MULTIPPLES FROM 5 TO 1000000

for number in range(0, 1000001):
    if (number % 5 == 0):
        print(number)

#this is commented out to not flood my terminal with the results
#while I test the rest of the program.

#SUMS ALL THE VALUES FROM A LIST AND PRINTS IT
a = [1, 2, 5, 10, 255, 3]
total = 0

for item in a:
    total += item;

print(total)

#PRINTS THE AVERAGE OF ALL THE NUMBERS OF A LIST

average = 0
newTotal = 0

for item in a:
    newTotal += item;

average = newTotal/len(a)
print(average)