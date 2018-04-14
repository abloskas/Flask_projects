# def scoreCalc():
#     for i in range(60, 100):
#         i.append(random.randint(60, 100))
#         print random.randint()
#     return score    
# scoreCalc()

# random_num = random.random()
# print random_num * 10
import random
i = random.randint(60, 100)
print i

def grades():
    for x in range(10):
        score = random.randint(60, 100)
        if score >= 60 and score <= 69:
            print "score: {}. Your grade is D".format(score)
        elif score >= 70 and score <= 79:
            print "score: {}. Your grade is C".format(score)    
        elif score >= 80 and score <= 89:
            print "score: {}. Your grade is B".format(score)     
        elif score >= 90 and score <= 100:
            print "score: {}. Your grade is A".format(score)
grades()               