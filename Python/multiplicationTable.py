line = "* ";

for number in range(1, 13):
    line = line + str(number) + " "
print(line)

for numy in range(1, 13):
    line = str(numy) + " ";
    for num in range(1, 13):
        line = line + str(numy * num) + " "
    print(line)