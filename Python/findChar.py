#input
word_list = ['hello','world','my','name','is','Anna']
new_list = []
char = 'o'

#output

for item in word_list:
    result = item.find('o')
    if (result > 0):
        new_list.append(item)

print(new_list)