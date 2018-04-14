# this function has one parameter(input)
# def say_hi(name):
#   print "Hi, " + name
# say_hi('Michael')
# say_hi('Anna')
# say_hi('Eli')

# def multiplycopy(arr,num):
#     for i in range(len(arr)):
#         arr[i] = arr[i]*num
#     print arr

# multiplycopy([2,4,10,16],5)
def random_coin_toss ():
	import random
	heads = 0
	tails = 0
	for i in range (5000):
		cointoss = round(random.random())
		print cointoss
		if (cointoss>.5):
			heads+=1
			print 'Attempt #{}: Its a head!! Got {} heads so far and {} tails so far'.format(i,heads,tails)
		else:
			tails+=1
			print 'Attempt #{}: Its a tail!! Got {} heads so far and {} tails so far'.format(i,heads,tails)

random_coin_toss()