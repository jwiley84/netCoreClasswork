users = {
'students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}],
'instructors': [
     {'first_name':  'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}]
}

def studentList(usrs):
    print('Students:')
    for student_num in range(0, len(usrs['students'])):
        total = len((usrs['students'][student_num]['first_name']) + (usrs['students'][student_num]['last_name']))
        print(str((student_num + 1)) + " - " + (usrs['students'][student_num]['first_name']) + " " + (usrs['students'][student_num]['last_name']) + " - " + str(total))
    print('Instructors:')
    for inst_num in range(0, len(usrs['instructors'])):
        total = len((usrs['instructors'][inst_num]['first_name']) + (usrs['instructors'][inst_num]['last_name']))
        print(str((inst_num + 1)) + " - " + (usrs['instructors'][inst_num]['first_name']) + " " + (usrs['instructors'][inst_num]['last_name']) + " - " + str(total))

studentList(users)

#print(users['students'])