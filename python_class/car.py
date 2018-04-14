
 # if price > 10000:
        #     self.tax = .15
        # else:
        #     self.tax = .12
class Car(object):
    def __init__(self, price, speed, fuel, mileage, tax):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax
        # self.display_all()

    def display_all(self):
        print "Price: " +  str(self.price)
        print "Speed: " + str(self.speed) + "mph"
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage) + "mpg"
        print "Tax: " + str(self.tax )             
        return self

mercGLC = Car(35000, 35, "full", 15, .15)
mercC300 = Car(25000, 35, "not full", 25, .15)
teslaS = Car(85000, 55, "full", 105, .15)
teslaX = Car(100000, 60, "not full", 110, .15)
bmwX3 = Car(9000, 25, "full", 20, .12)
bmwZ4 = Car(2000, 10, "kind of full", 10, .12)    

print mercGLC.display_all()   
print mercC300.display_all()
print teslaS.display_all()
print teslaX.display_all()
print bmwX3.display_all()
print bmwZ4.display_all()