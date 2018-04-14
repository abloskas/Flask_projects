# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def names(info):
#     for i in info:
#         print i['first_name'] + ' ' + i['last_name']
# names(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def namesTeachers(users):
    for key in users:
        print key
        count = 0
        for i in range (len(users[key])):
            count += 1
            fname =  users[key][i]['first_name']
            lname =  users[key][i]['last_name']
            char = len(fname)+len(lname)
            print '{} - {} {} - {}'.format(count, fname, lname, char)
namesTeachers (users)   

 


