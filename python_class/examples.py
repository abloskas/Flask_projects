string = "hello world"
print string.capitalize()
print string.upper()

string = "HELLO WORLD"
print string.lower()

string = "hello world hello world hello world"
print string.count('hello',0,100)

string = "hello world hello world hello world"
print string.find("llo",0,100)
# print string.index("baloon", 0,100)

string = "hello", "world", "this"
s = "help"
# print string.split("o", 1)

str = "hello world this is america"
print str.replace("world", "france")

str = "the sum of 2+2 is {}"
print str.format(2+5)

list = [1,2,3,4,5]
# print len(list)
# print max(list)
# print min(list)
# print list.index(3)
list.append(22)
print list
list.append("six")
print list

string = [1,2,3,4,5]
string.pop()
print string
string.pop(1)
print string
string = [1,2,3, "six"]
string.remove("six")
print string

string = [1,2,3]
string.insert(1, "six")
print string

string = ["six", "twelve", "two", 3]
string.sort()
print string
string.reverse()
print string

string =[1,2,3,4]
string2=["pop", "lock"]
string.extend(string2)
print string

string = [1,2,3,4]
string2=[5,6]
string.append(string2)
print string


aTuple = (123, 'xyz', 'zara', 'abc')
aList = list(aTuple)
print "List elements : ", aList
