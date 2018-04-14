L1 = [1,2,5,6,2]
L2 = [1,2,5,6,2] 
# l1 and l2 are the same

K1 = [1,2,5,6,5]
K2 = [1,2,5,6,5,3]
# k1 and k2 are not the same

J1 = [1,2,5,6,5,16]
J2 = [1,2,5,6,5]
# j1 and j2 are not the same

A1 = ['celery','carrots','bread','milk']
A2 = ['celery','carrots','bread','milk']
# a1 and a2 are the same


values = [[L1, L2], [K1, K2], [J1, J2], [A1, A2]]

for i in values:
    if i[0] == i[1]:
        print "these lists are the same"
    else:
        print "these lists are NOT the same"    