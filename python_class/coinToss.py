def coinToss():
    import random
    heads = 0
    tails = 0
    for i in range(5000):
        cointoss = random.randint(0,1)
        print cointoss
        if(cointoss >.5):
            tails += 1
            print "Attempt # {}: Throwing a coin... It's tails! ... Got {} head(s) so far and {} tail(s) so far".format(i, tails, heads)
        else:
            heads+= 1
            print "Attempt # {}: Throwing a coin... It's heads! ... Got {} head(s) so far and {} tail(s) so far".format(i, tails, heads)
coinToss()
