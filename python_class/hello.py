# # define a function that says hello to the name provided
# # this starts a new block
# def say_hello(name):
#   #these lines are indented therefore part of the function
#   name = "ash"
#   if name:
#    print 'Hello, ' + name + 'from inside the function'
#   else:
#    print 'No name'
# # now we're unindented and have ended the previous blockcopy
# print 'Outside of the function'

# age = 15
# if age >= 18:
#   print 'Legal age'
# else:
#   print 'You are so young!'

# for count in range (0,10):
#   print count

# list = [1,2,3,4,["six", "seven"],8,9]
# for element in list:
#   print element

# count = 0
# while count < 5:
#   print count
#   count += 1

# for val in "string":
#   if val == "i":
#     continue
#   print val

# x = 3
# y = x
# while y > 0:
#   print y
#   y = y - 1
# else:
#   print "Final else statement"

import md5 # imports the md5 module to generate a hash
password = 'password'
# encrypt the password we provided as 32 character string
hashed_password = md5.new(password).hexdigest()
print hashed_password #this will show you the hashed value
# 5f4dcc3b5aa765d61d8327deb882cf99 -> nice!


  
