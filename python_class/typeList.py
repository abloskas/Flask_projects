x = ['magical unicorns',19,'hello',98.98,'world']
y = [2,3,1,7,4,12]
z = ['magical','unicorns']

sum = 0
newStr = ''
for i in x:
    if isinstance(i, int) or isinstance(i, float):
        sum += i
    else:
        newStr += ' '+i 
# print sum, newStr  
if sum and newStr:
    print("The list you entered is of mixed type.")
    print("Sum: {}".format(sum))
    print("String:{}".format(newStr))
elif sum:
    print("The list you entered is of number type")
    print("Sum: {}".format(sum))
elif newStr:
    print("The list you entered is of string type")
    print("String: {}".format(newStr))
    print("")       
   


    