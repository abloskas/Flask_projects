# words = "It's thanksgiving day. It's my birthday,too!"
# print words.find('day')
# print words.replace('day','month')

# x = [2,54,-2,7,12,98]
# print max(x)
# print min(x)

# x = ["hello",2,54,-2,7,12,98,"world"]
# print x[-1]
# print x[0]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
y = x[:len(x)/2] 
z = x[len(x)/2:] 
print y
print z
z.insert(0,y)
print z