class Call(object):
    def __init__(self, uniqueID, callerName, callerNumber, time, reason): 
        self.uniqueID = uniqueID
        self.callerName = callerName
        self.callerNumber = callerNumber
        self.time = time
        self.reason = ''

    def display(self):
        print self.uniqueID
        print self.callerName
        print self.callerNumber
        print self.time
        print self.reason

class CallCenter(object):
    def __init__(self):
        self.callList = []
        self.queueSize = len(self.callList)       

    def add(self, call):
        self.callList.append(call)
        self.queueSize += 1
        return self

    def remove(self):
        self.callList.pop(0)
        self.queueSize -= 1
        return self

    def info(self):
        for calls in self.callList:
            print calls.callerName, calls.callerNumber
        print "length of queue {}".format(self.queueSize)


CC = CallCenter()
CC.add(Call(12, "sam", 911, 400, "bored at work")).info()
CC.add(Call(172, "ashley", 5550987, 100, "bored at home")).info()




