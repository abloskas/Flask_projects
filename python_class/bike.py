class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):  
        print self.price
        print self.max_speed
        print self.miles
        return self  

    def ride(self):
        self.miles += 10
        print "Riding"
        return self

    def reverse(self):
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        print "Reversing"
        return self

bike1 = Bike(200, "25mph")
bike2 = Bike(150, "15mph")
bike3 = Bike(175, "20mph")

print bike1.ride().ride().ride().reverse().displayInfo()   
print bike2.ride().ride().reverse().reverse().displayInfo()
print bike3.reverse().reverse().reverse().displayInfo()   
            