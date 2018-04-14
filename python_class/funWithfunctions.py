def odd_even():
    for i in range(1,2001):
        if i%2 == 0:
            print 'number is {}. this is an even number.'.format(i)
        else:
            print 'number is {}. this is an odd number.'.format(i)
odd_even()                

# Number is 1.  This is an odd number.
# Number is 2.  This is an even number.
# Number is 3.  This is an odd number.
# ...
# Number is 2000.  This is an even number.

def multiply(list,num):
    for i in range(len(list)):
        list[i] = list[i]*num
    print list
multiply([2,4,10,16],5)


def layered_multiples(list, num):
    newList = []
    for i in range(len(list)):
        list[i] = list[i]*num
        newList2 = []
        for x in range(0, list[i]):
            newList2.append(1)
        newList.append(newList2)    
    print newList
layered_multiples([2,4,5],3)


# def layered_multiples(arr):
#   # your code here
#   return new_array
# x = layered_multiples(multiply([2,4,5],3))
# print x
# # output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]





