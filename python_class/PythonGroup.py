# 1.
# SET greeting AS 'hello' 
greeting = 'hello'
# SET name AS 'dojo' 
name = 'dojo'
# LOG name + greeting
print name + greeting
# 2.
# Given an array of words: ['Wish', 'Mop', 'Bleet', 'March', 'Jerk']
words = ['Wish', 'Mop', 'Bleet', 'March', 'Jerk']
# Loop through the array
for x in words:
# Print each word to consol
    print x
# 3.
# Write a function that takes a number.

def jam():
    val = [2,3,5,3, 5]
    whatever = []
    for x in range(0, 5):
        for i in range (len(val)): 
            val[i] = val[i]*2
            whatever.append(val[i])
        print whatever
        x = x + 1
jam()
# Create an empty list.

# Multiply that number by 2.
# Push the new number to our empty list.
# Repeat 25 times.
# Print list.


# 4.
# Define a small program that accepts strings as inputs
def newProgram (string):
    newString = ""
    for i in range(len(string)-1, -1, -1):
        newString+=string[i]
    print newString
    return newString

newProgram('hello')
    
# Have your program create a blank string.

# Starting at the back of the input string and walking backwards: 3a. Push each character into the blank string. 3b. Repeat for all characters in input string.
# Print the reversed string.
# 5.

x = 10
x = x*7
y = 30 
z = y+x
z = z*3
z = z-y
z = z/275
x = z+y
y = 3 
x = x + y

if x % 10 == 0:
    print "true"
else:
    print "false"
# x EQUALS 10
# x EQUALS x TIMES 7
# y EQUALS 30
# z EQUALS y PLUS x
# z EQUALS z TIMES 3
# z EQUALS z MINUS y
# z EQUALS z DIVIDED_BY 27S
# x EQUALS z PLUS y
# y EQUALS 3
# x EQUALS x PLUS y
# RETURN TRUE if x MODULUS 10 EQUALS 0
# OTHERWISE RETURN FALSE