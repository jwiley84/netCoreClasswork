a = 0;

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
list_one2 = [1,2,5,6,5]
list_two2 = [1,2,5,6,5,3]
list_one3 = [1,2,5,6,5,16]
list_two3 = [1,2,5,6,5]
list_one4 = ['celery','carrots','bread','milk']
list_two4 = ['celery','carrots','bread','cream']



if (len(list_one4) == len(list_two4)):
    for item in range(0, len(list_two4)):
        if (list_one4[item] == list_two4[item]):
            a += 1; 
else:
    print("they don't match!")

#print(a)
#print(len(list_one2))
if (a == len(list_one4)):
    print("They match!")
else:
    print("they don't match here!")