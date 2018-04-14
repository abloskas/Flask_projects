aboutMe = {'name':'Ashley', 'age':'25', 'country of birth':'Murica', 'favorite language':'Murican'}

def personalInfo(info):
    for key in info:
        print "My {} is {}".format(key,info[key])
personalInfo(aboutMe)